import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_location = "/Users/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.nlb.gov.sg/main/home")
driver.maximize_window()

# click to view the ratings available for selection
driver.find_element(By.CLASS_NAME, '//*[@id="wog--sentiments-content"]/wog-tabbed-widget/div/div').click()

# click the 6th rating that represents "Very Stisfied"
rating_choice = '//*[@id="wog--sentiments-content"]/wog-rating/div/div/div[2]/wog-emoji-rating-scale-field/div/div[1]/div[6]/button/svg/path[1]'
driver.find_element_by_xpath(rating_choice).click()
time.sleep(4)

# close "Tell us more" pop-up
popUp = '//*[@id="wog--sentiments-content"]/wog-modern-feedback/div/wog-close-button/button/svg/line[1]'
driver.find_element_by_xpath(popUp).click()

time.sleep(5)