from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

driver = webdriver.Chrome('/Users/deinm/Downloads/chromedriver')
driver.implicitly_wait(3)

loginID = 'YourID'
loginPWD = 'YourPW'


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path='/Users/deinm/Downloads/chromedriver')

driver.get('https://www.facebook.com')
driver.find_element_by_name('email').send_keys(loginID)
driver.find_element_by_name('pass').send_keys(loginPWD)

try:
    driver.find_element_by_name('login').click()
except Exception:
    driver.find_element_by_id('loginbutton').click()

driver.implicitly_wait(7)
driver.get('https://www.facebook.com/pg/%EB%B2%84%EC%8A%A4-%EC%A0%95%EB%A5%98%EC%9E%A5-%ED%9D%A1%EC%97%B0-%ED%86%B5%EA%B3%84-%EC%95%8C%EB%A6%BC-103071191104097/posts/?ref=page_internal')
driver.implicitly_wait(7)

article = '2019년 10월 5일 버스 정류장 흡연 감지 통계입니다.\n1.(성동구) 뚝섬서울숲(응봉사거리 방면) 12건'


driver.find_element_by_class_name('_3hvt').click()
driver.find_element_by_class_name('_5yk2').click()
driver.find_element_by_class_name('_5yk2').send_keys(article)
driver.implicitly_wait(7)

driver.find_element_by_xpath('//*[@id="composerPostButton"]/div/button').click()


# 사진 올리기
'''
driver.get('https://www.facebook.com/pg/%EB%B2%84%EC%8A%A4-%EC%A0%95%EB%A5%98%EC%9E%A5-%ED%9D%A1%EC%97%B0-%ED%86%B5%EA%B3%84-%EC%95%8C%EB%A6%BC-103071191104097/posts/?ref=page_internal')
driver.implicitly_wait(7)

# Click the post box
driver.find_element_by_class_name('_2aha').click()
driver.find_element_by_class_name('_51mx').click()
'''
