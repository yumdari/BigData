from selenium import webdriver
from selenium.webdriver.common.by import By # for using By instead of 'find_element_by_css_selector' method

driver = webdriver.Chrome('C:/Workspace/chromedriver')
driver.implicitly_wait(3)
driver.get("http://www.yes24.com/Product/goods/40936880")
import time
time.sleep(2)
readLinks = driver.find_elements(By.CSS_SELECTOR,"#infoset_reviewContentList div.btn_halfMore > a") # 펼쳐보기

for readlink in readLinks :
    readlink.click()
    time.sleep(1)
reviewList = driver.find_elements(By.CSS_SELECTOR,"#infoset_reviewContentList div.reviewInfoBot.origin div.review_cont")

temp_list = []
time.sleep(3)
for review in reviewList :
    temp_list.append(review.text)
stopFlag = False
while True :
    for n in range(4, 13) :
        linkurl = '#infoset_reviewContentList > div.review_sort.sortBot >div.review_sortLft > div > a:nth-child('+str(n)+')'
        linkNum = driver.find_element(By.CSS_SELECTOR,linkurl)
        linkNum.click()
        time.sleep(3)
readLinks = driver.find_elements(By.CSS_SELECTOR,"#infoset_reviewContentList div.btn_halfMore > a")
for readlink in readLinks :
    #readlink.click()
    driver.execute_script("arguments[0].click();", readlink)
    time.sleep(3)
    
reviewList = driver.find_elements(By.CSS_SELECTOR,"#infoset_reviewContentList div.reviewInfoBot.origindiv.review_cont")
time.sleep(2)

for review in reviewList :
    temp_list.append(review.text)

if len(reviewList) < 5 :
    stopFlag = True
    break
if stopFlag == True :
    break
nextPage = '#infoset_reviewContentList > div.review_sort.sortBot >div.review_sortLft > div >a.bgYUI.next'
linkNum = driver.find_element(By.CSS_SELECTOR,nextPage)
linkNum.click()
time.sleep(1)

for item in temp_list :
    print(item)
    
wfile = open("c:/Temp/서점file.txt","w")
wfile.writelines(temp_list)
wfile.close()
