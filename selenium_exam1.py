from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/workspace/chromedriver')
print("webdriver 객체 : ", type(driver))

driver.get('http://www.google.com/ncr')
target = driver.find_element(By.CSS_SELECTOR,"[name='q']")
print("태그 객체 : ", type(target))
target.send_keys('파이썬')
target.send_keys(Keys.ENTER)
#diver.quit(0)