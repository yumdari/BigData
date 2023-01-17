import requests
from bs4 import BeautifulSoup
title = []
link = []
urlstr = 'http://www.yes24.com/SearchCorner/Search?domain=BOOK&query=python'
r = requests.get(urlstr)
r.encoding = "utf-8"
bs = BeautifulSoup(r.text, 'html.parser')
titleList = bs.select('div.info_row.info_name > a')
linklList = bs.select('div.info_row.info_name > a')

for titleDom in titleList :
    title.append(titleDom.string)
for linkDom in linklList :
    link.append(linkDom["href"])
    
print("-- 도서 제목 --")
print(title)
print("-- 도서 링크 URL --")
print(link)