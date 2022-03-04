from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://youtube.com')

searchbox = driver.find_element('id',"search")
driver.implicitly_wait(10)
print(searchbox);
searchbox.set_attribute('value', 'Python advanced')

# searchButton = driver.find_element('//*[@id="search-icon-legacy"]')
# searchbox.click()

# ActionChains(driver).move_to_element(button).click(button).perform()