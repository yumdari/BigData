from urllib.request import urlopen
response = urlopen("http://www.naver.com")
print(response)
print("[header 정보]----------")
res_header = response.getheaders()
for idx in res_header : 
    print(idx)
print("[body 내용]----------")
#print(response.read())
print(response.read().decode('utf-8'))