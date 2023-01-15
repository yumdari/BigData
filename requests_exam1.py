import requests
r = requests.request('get','http://www.naver.com')
r.encoding = 'utf-8'
print(type(r))
if r.text : 
    print(r.text)
else :
    print('응답된 콘텐츠가 없어요')
print('------------------------------------------------------------')
r = requests.request('head','http://www.naver.com')
r.encoding = 'utf-8'
print(type(r))
if r.text :
    print(r.text)
else :
    print('응답된 콘텐츠가 없어요')
print('------------------------------------------------------------')
r = requests.request('post','http://www.naver.com', data={'name':'백도','age':12})
r.encoding = 'utf-8'
print(type(r))
if r.text :
    print(r.text)
else :
    print('응답된 콘텐츠가 없어요')