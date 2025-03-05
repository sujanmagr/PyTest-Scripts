#simple login page
from selenium.webdriver.common.by import By

class loginpage:
    def __init__(self, driver):
        self.driver=driver
        self.username_textbox=(By.XPATH,"//input[@id='user-name']")
        self.password_textbox=(By.XPATH,"//input[@id='password']")
        self.login_button=(By.XPATH,"//input[@id='login-button']")
    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

        