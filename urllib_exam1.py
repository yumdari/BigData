from urllib.request import urlopen
response = urlopen('http://www.naver.com/')
print(type(response))
print(response.status)
print(response.version)
print(response.msg)
res_header = response.getheaders()
print("[header 정보]----------")
for idx in res_header : 
    print(idx)