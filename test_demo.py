#script to search something and click on the first link appear
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")

def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_google(browser):
    url="https://duckduckgo.com"
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    # assert "Google" in browser.title, f"Expected 'Google' as title but got '{browser.title}'" 
    time.sleep(3)
    search=browser.find_element(*(By.XPATH,"//input[@id='searchbox_input']"))
    search.send_keys("skill shiksha")
    time.sleep(4)
    # enter=browser.find_element(*(By.XPATH,"//div[@class='lJ9FBc']//input[@name='btnK']"))
    # enter.click()
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    first=browser.find_element(*(By.XPATH,"//article[@id='r1-0']//div[@class='OQ_6vPwNhCeusNiEDcGp']"))
    first.click()
    time.sleep(2)

