from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:workspace/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.starbucks.co.kr/store/store_map.do?disp=quick")

#target = driver.find_element_by_class_name("quickResultLstCon") no more find_element_by_class_name
target = driver.find_element(By.CLASS_NAME,"quickResultLstCon")

print(type(target))
print(type(target.text))
print(target.text)
driver.quit()