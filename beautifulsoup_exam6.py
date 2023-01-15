html_doc = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8>
        <title>Test BeautifulSoup</title>
    </head>
    <body>
       <p align="center"> text contents </p>
       <p align="right" class="myp"> text contents 2 </p>
       <p align="left" a="b"> text contents 3 </p>
       <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" width="500">
       <div>
        <p>text contents 4</p>
       </div>
    </body>
</html>
</html> """
from bs4 import BeautifulSoup
bs = BeautifulSoup(html_doc, 'html.parser')
print(bs.find('p', align="center"))
print(bs.find('p', class_ = "myp"))
print(bs.find('p', align = "left"))
print("------------------------------")
print(bs.find('p', attrs={"align":"center"}))
print(bs.find('p', attrs={"align":"right", "class":"myp"}))
print(bs.find('p', attrs={"align":"left"}))