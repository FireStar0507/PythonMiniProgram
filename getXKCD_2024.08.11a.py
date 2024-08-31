#!  Python3

from pathlib import Path
from shutil import rmtree, move
import requests as req
import bs4 
from os import makedirs, rmdir
from os.path import join as osjoin, basename as osbasename


httpUrl = r"https://xkcd.com/2971/"  # 添加 /
nothings = 0
comicNum = 0
oldName = []
newName = []
XKCDpath = Path("XKCD")
if XKCDpath.is_dir():
    rmtree("XKCD")
makedirs("XKCD")
makedirs("_XKCD_")


while not httpUrl.endswith("#"):
    comicNum += 1
    print(f"正在解析网页 {httpUrl}…")
    httpRes = req.get(httpUrl)
    httpRes.raise_for_status()

    soup = bs4.BeautifulSoup(httpRes.text, "html.parser")
    comicElem = soup.select("#comic img")
    if comicElem:
        comicUrl = "https:" + comicElem[0].get("src")
        print(f"正在下载图像 {comicUrl}…")
        comicRes = req.get(comicUrl)
        comicRes.raise_for_status()
        filename = osbasename(comicUrl)
        oldName.insert(0, filename)

        comicFile = open(osjoin("_XKCD_", filename), "wb")
        for chunk in comicRes.iter_content(100000):
            comicFile.write(chunk)
        comicFile.close()
    else:
        print("没有寻找到图像")
        oldName.insert(0, "")
        nothings += 1

    prevLink = soup.select('a[rel="prev"]')[0]  # 修改选择器语法
    httpUrl = "https://xkcd.com" + prevLink.get("href")  # 使用正确的域名


print(f"一共解析了 {comicNum} 次网页\n下载了 {comicNum - nothings} 张漫画\n其中有 {nothings} 个网页没有寻找到漫画")

# 使用 enumerate 和列表推导式简化循环
newName = [f"XKCD{i+1}_{name}" if name else "" for i, name in enumerate(oldName)]

for old, new in zip(oldName, newName):
    if new:
        print(f"正在将图像 {old} 处理为 {new}…")
        move(osjoin("_XKCD_", old), osjoin("XKCD", new))
rmdir("_XKCD_")


print("完成")

