from selenium import webdriver

url = 'http://www.nbaminer.com/player-shot-zones/'
driver = webdriver.Chrome("/Users/Hallshit/Downloads/chromedriver")
driver.get(url)

name = 'Daminan Lillard'

driver.execute_script("window.scrollTo(0, 200)")

searchbar = driver.find_element_by_xpath('//*[@id="quick-filter-toolbar"]/div/div/input')
searchbar.send_keys(name)

driver.close()