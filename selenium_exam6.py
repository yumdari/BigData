from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('haedless') # browser 기동시키지 않음 - headless 모드
options.add_argument('window-size = 1920x1080')
driver = webdriver.Chrome('C:/workspace/chromedriver', options = options)

driver.get('http://www.python.org/')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('C:/workspace/main_main_headless.png')
print('캡처 저장 완료')
import time
time.sleep(2)
driver.quit()