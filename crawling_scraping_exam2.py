import requests
from bs4 import BeautifulSoup
import re
for n in range(1,31) :
    req = requests.get('http://movie.naver.com/movie/point/af/list.nhn?page='+str(n))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('.movie')
    points = soup.select('td.title > div > em')
    reviews = soup.select('td.title')
    movie_title = []
    movie_point = []
    movie_review = []
for dom in titles :
    movie_title.append(dom.text)
for dom in points :
    movie_point.append(dom.text)
for dom in reviews :
    content = dom.contents[6]
    content = re.sub("신고",'', content)
    content = re.sub("[\n\t]",'',content)
    movie_review.append(content)
    
commentLength = len(movie_title)
for idx in range(commentLength) :
    print(movie_point[idx] + "\t" + movie_title[idx] + "\t" + movie_review[idx])
print("-------------------------------------------------------")