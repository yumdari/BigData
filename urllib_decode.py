from urllib.request import urlopen
response = urlopen('http://www.naver.com')
response.read().decode("utf-8")