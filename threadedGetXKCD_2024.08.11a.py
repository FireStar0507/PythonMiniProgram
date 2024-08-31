# --- 主程序 ---
XKCDpath = Path("XKCD")
if XKCDpath.is_dir():
    rmtree("XKCD")
makedirs("XKCD")
makedirs("_XKCD_")

while not httpUrl.endswith("#"):
    comicNum += 1
    print(f"正在解析网页 {httpUrl}…")

    httpRes = fetch_comic_page(httpUrl)
    if httpRes is None:
        print(f"无法访问 {httpUrl}, 结束程序.")
        break

    soup = bs4.BeautifulSoup(httpRes.text, "html.parser")
    comicElem = soup.select("#comic img")
    if comicElem:
        comicUrl = "https:" + comicElem[0].get("src")
        filename = osbasename(comicUrl)
        oldName.insert(0, filename)

        # 创建并启动下载线程
        download_thread = threading.Thread(target=download_comic, args=(comicUrl, filename))
        download_threads.append(download_thread)
        download_thread.start()

        # 控制线程数量
        if len(download_threads) >= max_threads:
            for t in download_threads:
                t.join()
            download_threads = []
    else:
        print("没有寻找到图像")
        oldName.insert(0, "")
        nothings += 1

    prevLink = soup.select('a[rel="prev"]')
    if prevLink:
        httpUrl = "https://xkcd.com" + prevLink[0].get("href")
    else:
        break

# 等待所有线程完成
for t in download_threads:
    t.join()

print(f"一共解析了 {comicNum} 次网页\n下载了{comicNum - nothings}张漫画\n其中有 {nothings} 个网页没有寻找到漫画")

newName = [f"XKCD{i+1}_{name}" if name else "" for i, name in enumerate(oldName)]

for old, new in zip(oldName, newName):
    if new:
        source_path = osjoin("_XKCD_", old)
        destination_path = osjoin("XKCD", new)
        
        if Path(source_path).exists():
            print(f"正在将图像 {old} 处理为 {new}…")
            try:
                move(source_path, destination_path)
            except Exception as e:
                print(f"移动文件时出错: {e}")
        else:
            print(f"文件 {source_path} 不存在，无法移动。")
            
rmdir("_XKCD_")

print("完成")
