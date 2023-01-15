html_doc = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Test BeautifulSoup</title>
    </head>
    <body>
        <h1>Test</h1>
    </body>
</html> """
from bs4 import BeautifulSoup
bs = BeautifulSoup(html_doc, 'html.parser')
print(type(bs))