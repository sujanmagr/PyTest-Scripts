from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pom.page.login_page import loginpage
from pom.page.yourself_page import yourself
from pom.page.contact_page import contact

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_login(driver):
    login_page=loginpage(driver)
    login_page.open_page("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(3)

    login_page.enter_username("standard_user")
    time.sleep(1)

    login_page.enter_password("secret_sauce")
    time.sleep(1)

    login_page.click_login()
    time.sleep(4)

#test script for yourself page
def test_yourself(driver):
    yourself_page=yourself(driver)
    yourself_page.open_page("https://sagar-test-qa.vercel.app/about.html")
    driver.maximize_window()
    time.sleep(2)

    yourself_page.enter_fullname("sujan budhathoki")
    time.sleep(1)

    yourself_page.enter_phone("9805125187")
    time.sleep(1)

    yourself_page.enter_email("sujan@gmail.com")
    time.sleep(1)

    yourself_page.enter_hobby("software testing and api testing")
    time.sleep(1)

#contact page
def test_contact(driver):
    contact_page=contact(driver)
    contact_page.open_page("https://sagar-test-qa.vercel.app/contact.html")
    driver.maximize_window()
    time.sleep(2)

    contact_page.enter_name("sujan budhathoki")
    time.sleep(1)

    contact_page.enter_email("abcd@gmail.com")
    time.sleep(1)

    contact_page.enter_message("its a good page")
    time.sleep(1)

