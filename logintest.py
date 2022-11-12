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

    # navigate to login page
    driver.find_element(by=By.CSS_SELECTOR, value="a[href='https://cassamv2.nlb.gov.sg/cas/login?service=https%3a%2f%2fwww.nlb.gov.sg%2fmylibrary%2fcas&applicationId=NLB']").click()
    time.sleep(5)

    # enter username
    enter_username = driver.find_element(by=By.NAME, value="username")
    enter_username.send_keys("devOpsTeam4")
    time.sleep(3)

    enter_password = driver.find_element(by=By.NAME, value="password")
    enter_password.send_keys("devOps2022!")
    time.sleep(3)

    # click submit
    driver.find_element(by=By.NAME, value="submit").click()
    time.sleep(5)

    driver.quit()
