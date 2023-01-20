from selenium import webdriver
driver = webdriver.Chrome('C:workspace/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.starbucks.co.kr/store/store_map.do?disp=quick")
import time
time.sleep(2)
loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(2)
f_link = driver.find_element_by_css_selector("div.loca_step1_cont > ul > li:nth-child(1) > a")
f_link.click()
time.sleep(2)
s_link = driver.find_element_by_css_selector("#mCSB_2_container > ul > li:nth-child(1) > a")
s_link.click()
time.sleep(2)
shopList = driver.find_elements_by_css_selector("#mCSB_3_container > ul > li")
temp_list = []
time.sleep(3)
count = 0
total = len(shopList)
for shop in shopList : 
    count += 1
    shoplat = shop.get_attribute("data-lat")
    shoplong = shop.get_attribute("date-long")

shopname = shop.find_element_by_tag_name("strong")
shopinfo = shop.find_element_by_tag_name("p")
splitinfo = shopinfo.text.split('\n')
if(len(splitinfo) == 2) :
    addr = splitinfo[0]
    phonenum = splitinfo[1]
temp_list.append([shopname.text, shoplat, addr, phonenum])
if count != total and count % 3 == 0 :
    driver.execute_script("var su = arguments[0]; var dom = document.querySelectorAll('#mCSB_3_container > ul > li')[su]; dom.scrollIntoView();",count)
    
for item in temp_list :
    print(item)