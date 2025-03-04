from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest
import random
import re
import string

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visua_user", "secret_sauce"),#wrong user
])
def test_login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    
    # Wait for the page to load and find elements
    username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    
    # Clear fields to prevent any previous values
    username_field.clear()
    password_field.clear()
    
    # Fill in the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Click login button
    login_button.click()
    time.sleep(2)
    
    try:
        # Check if login was successful
        if "product" in driver.page_source:
            print("Login successful!")
            assert True  # Login successful
        else:
            raise AssertionError("Login failed - 'product' not found in page source.")
    
    except Exception as e:
        print(f"Error! {str(e)}")
        assert False  # Fail the test if there's an error

