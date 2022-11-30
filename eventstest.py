import time

from selenium import webdriver

chromedriver_location = "/Users/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.nlb.gov.sg/main/home")
driver.maximize_window()

# navigate to "what's On" page
page = '//*[@id="discover-menu-name-80"]'
driver.find_element_by_xpath(page).click()

# choose type of event
type = '//*[@id="interestForm"]/div/form/div/div[2]/a/input'
driver.find_element_by_xpath(type).click()

# choose "Workshop"
type_workshop = '//*[@id="interestForm"]/div/form/div/div[2]/div/ul/li[10]/a'
driver.find_element_by_xpath(type_workshop).click()

# click "Go"
go_button = '//*[@id="filterRedirect"]'
driver.find_element_by_xpath(go_button).click()

time.sleep(5)