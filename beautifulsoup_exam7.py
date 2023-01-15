import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com')
html = req.content
print(type(html))
html = html.decode('utf-8')
#print(html)
print("========================================")
bs = BeautifulSoup(html, 'html.parser')
title = bs.select('h1')
title1 = bs.select('#f_subtitle')
title2 = bs.select('.subtitle')
title3 = bs.select('aside > h2')
img = bs.select('[src]')

print(type(title))
print(type(title[0]))
print("<h1>태그의 개수 : %d" %len(title))
print("f_subtitle이라는 id 속성을 갖는 태그 개수 : %d" %len(title1))
print("subtitle이라는 class 속성을 갖는 태그 개수 : %d" %len(title2))
print("aside 태그의 <h2> 자식 태그 개수 : %d" %len(title3))
print("src 속성을 갖는 태그 개수 : %d" %len(img))

for content in title : 
    print(content.string)
print("------------------------------")
for content in title1 : 
    print(content.text)
print("------------------------------")
for content in title2 : 
    print(content.text)
print("------------------------------")
for content in title3 : 
    print(content.text)
print("------------------------------")
for content in img : 
    print(content["src"])