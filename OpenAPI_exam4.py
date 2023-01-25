import urllib.request
import json
client_key = '부여 받은 Client ID'
client_secret = '부여 받은 Client Secret'
query = '치맥'
encText = urllib.parse.quote_plus(query)

num = 100
naver_url = 'https://openapi.naver.com/v1/search/news.json?query='+encText+'&display='+str(num)
request = urllib.request.Request(naver_url)
request.add_header("X-Naver-Client-Id", client_key)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode == 200) :
    response_body = response.read()
    dataList = json.loads(response_body)
    count = 1
    print('['+query+'에 대한 포털사이트 뉴스 글]')
    for data in dataList['items']:
        print(str(count)+':'+data['title'])
        print('['+data['description']+']')
        count+=1
    else :
        print('오류 코드 : '+rescode)