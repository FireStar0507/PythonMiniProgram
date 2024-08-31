from webbrowser import open
text = input("")
url = {"bing":"https://cn.bing.com/search?q=",
       "baidu":"https://www.baidu.com/s?&wd=",
       "bilibili":"https://search.bilibili.com/all?keyword="}
open(url["bing"] + text)
open(url["baidu"] + text)
open(url["bilibili"] + text)
