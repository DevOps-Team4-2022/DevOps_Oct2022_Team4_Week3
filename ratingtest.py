import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.nlb.gov.sg/main/home")
driver.maximize_window()

# click to view the ratings available for selection
see_rating_choices = '//*[@id="wog--sentiments-content"]/wog-tabbed-widget/div/div/p'
driver.find_element_by_xpath(see_rating_choices).click()

# click the 6th rating that represents "Very Stisfied"
rating_choice = '//*[@id="wog--sentiments-content"]/wog-rating/div/div/div[2]/wog-emoji-rating-scale-field/div/div[1]/div[6]/button/svg/path[2]'
driver.find_element_by_xpath(rating_choice).click()

time.sleep(5)