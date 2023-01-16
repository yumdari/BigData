import requests
from bs4 import BeautifulSoup
title = []
link = []
urlstr = 'http://www.yes24.com/SearchCorner/Search?domain=BOOK&query=python'
r = requests.get(urlstr)
#r.encoding = "utf-8"
bs = BeautifulSoup(r.text, 'html.parser')
titleList = bs.select('p.goods_name.goods_icon > a > strong')
linklList = bs.select('p.goods_name.goods_icon > a')

for titleDom in titleList :
    title.append(titleDom.string)
for linkDom in linklList :
    link.append(linkDom["href"])
    
print("-- 도서 제목 --")
print(title)
print("-- 도서 링크 URL --")
print(link)