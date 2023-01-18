import requests
from bs4 import BeautifulSoup
session = requests.session()
login_info = {
    "m_id" : "",
    "m_passwd" : ""
}

url_login = "http://www.hanbit.co.kr/member/login.html"
res = session.post(url_login, data =login_info)
res.raise_for_status()

url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
print(soup)
# mileage = soup.select_one(".mileage_section1 span").get_text()
# ecoin = soup.select_one(".mileage_section2 span").get_text()
# print("마일리지:" + mileage)
# print("이코인:" + ecoin)