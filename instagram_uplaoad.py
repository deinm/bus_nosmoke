from selenium import webdriver
driver = webdriver.Chrome('/Users/deinm/Downloads/chromedriver')
driver.implicitly_wait(3)

loginID = 'donot.smoke.on.street'
loginPWD = 'street1248'

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
driver.find_element_by_name('username').send_keys(loginID)
driver.find_element_by_name('password').send_keys(loginPWD)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

driver.implicitly_wait(3)

driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span').click()