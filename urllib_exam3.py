from urllib.request import urlopen
print("========================================================================================================================")
url = 'https://www.python.org/'
f = urlopen(url)
print(type(f))
print(type(f.info()))
encoding = f.info().get_content_charset()
print(url, 'encoding information of page : ', encoding)
text = f.read(500).decode(encoding)
print(text)
print("========================================================================================================================")