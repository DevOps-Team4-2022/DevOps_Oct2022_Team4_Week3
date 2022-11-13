import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_eight_components():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get("https://www.nlb.gov.sg/main/home")
    driver.maximize_window()

    title = driver.title
    assert title == "Home" #Page title (Look at tab for page title)
    driver.implicitly_wait(0.5)

    # search devops book
    search_box = driver.find_element(by=By.ID, value="searchBox")
    search_box.send_keys("devops paradox")
    time.sleep(1)

    # click submit
    driver.find_element(By.CSS_SELECTOR, '#interestSearch > div > form > div > div > div > div > button').click()
    time.sleep(1)

    # switch to new page
    driver.switch_to.window(driver.window_handles[1])

    # click on book
    driver.find_element(By.CSS_SELECTOR, "[title='DevOps paradox : the truth about DevOps by the people on the front line / Viktor Farcic. ']").click()

    # switch to new page
    driver.switch_to.window(driver.window_handles[2])

    # check that current page is https://catalogue.nlb.gov.sg/cgi-bin/spydus.exe/ENQ/WPAC/BIBENQ?SETLVL=1&BRN=204304526
    get_url = driver.current_url
    assert get_url == "https://catalogue.nlb.gov.sg/cgi-bin/spydus.exe/ENQ/WPAC/BIBENQ?SETLVL=1&BRN=204304526"

    driver.quit()
