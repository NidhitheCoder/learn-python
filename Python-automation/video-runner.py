from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://youtube.com')

searchbox = driver.find_element('//*[@id="search"]')
searchbox.send_keys('Python advanced')

searchButton = driver.find_element('//*[@id="search-icon-legacy"]')
searchbox.click()