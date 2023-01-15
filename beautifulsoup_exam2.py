html_doc = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8>
        <title>Test BeautifulSoup</title>
    </head>
    <body>
        <p align="center">P태그의 콘텐츠</p>
        <img src=https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"width="300">
    </body>
</html>"""
from bs4 import BeautifulSoup
bs = BeautifulSoup(html_doc, 'html.parser')
print(bs.prettify())