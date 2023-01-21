from selenium import webdriver
from selenium.webdriver.common.by import By # for using By instead of 'find_element_by_css_selector' method
driver = webdriver.Chrome('C:workspace/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.starbucks.co.kr/store/store_map.do?disp=quick")

import time
time.sleep(2)

#loca = driver.find_element_by_class_name('loca_search') # no more use find_element_by_class_name
loca = driver.find_element(By.CLASS_NAME,"loca_search") # 지역 검색
loca.click()
time.sleep(2)

#f_link = driver.find_element_by_css_selector("div.loca_step1_cont > ul > li:nth-child(1) > a") # no more use find_element_by_css_selector
f_link = driver.find_element(By.CSS_SELECTOR,"div.loca_step1_cont > ul > li:nth-child(1) > a") # 서울
f_link.click()
time.sleep(2)

#s_link = driver.find_element_by_css_selector("#mCSB_2_container > ul > li:nth-child(1) > a") # no more use find_element_by_css_selector
s_link = driver.find_element(By.CSS_SELECTOR,"#mCSB_2_container > ul > li:nth-child(1) > a")
s_link.click()
time.sleep(2)

#shopList = driver.find_elements_by_css_selector("#mCSB_3_container > ul > li") # no more use find_element_by_css_selector
shopList = driver.find_element(By.CSS_SELECTOR,"#mCSB_3_container > ul > li")
temp_list = []
time.sleep(3)



count = 0
total = len(shopList)
for shop in shopList : 
    count += 1
    shoplat = shop.get_attribute("data-lat")
    shoplong = shop.get_attribute("data-long")

shopname = shop.find_element(By.TAG_NAME,"strong")
shopinfo = shop.find_element(By.TAG_NAME,"p")

splitinfo = shopinfo.text.split('\n')
if(len(splitinfo) == 2) :
    addr = splitinfo[0]
    phonenum = splitinfo[1]
temp_list.append([shopname.text, shoplat, addr, phonenum])
if count != total and count % 3 == 0 :
    driver.execute_script("var su = arguments[0]; var dom = document.querySelectorAll('#mCSB_3_container > ul > li')[su]; dom.scrollIntoView();",count)
    
for item in temp_list :
    print(item)