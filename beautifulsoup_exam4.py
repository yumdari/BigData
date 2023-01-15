html_doc = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8>
        <title>Test BeautifulSoup</title>
    </head>
    <body>
        <p align="center">P태그의 콘텐츠</p>
        <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" width="300">
        <ul>
            <li>테스트1<strong>강조</strong></li>
            <li>테스트2</li>
            <li>테스트3</li>
        </ul>
    </body>
</html> """
from bs4 import BeautifulSoup
bs = BeautifulSoup(html_doc, 'html.parser')
print("[string 속성]")
print(type(bs.p.string), ':', bs.p.string)
print(type(bs.ul.string), ':', bs.ul.string)
print(type(bs.ul.li.string), ':', bs.ul.li.string)
print(type(bs.ul.li.strong.string), ':', bs.ul.li.strong.string)