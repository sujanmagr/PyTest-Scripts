#script to fillup contact me page
from selenium.webdriver.common.by import By

class contact():
    def __init__(self, driver):
        self.driver=driver
        # self.driver.execute_script("window.scrollBy(0,300);")
        self.name_textbox=(By.XPATH,"//input[@id='name']")
        self.email_textbox=(By.XPATH,"//input[@id='email']")
        self.message_textbox=(By.XPATH,"//textarea[@id='message']")
    
    def open_page(self, url):
        self.driver.get(url)
    
    def enter_name(self, name):
        self.driver.find_element(*self.name_textbox).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)
    
    def enter_message(self, message):
        self.driver.find_element(*self.message_textbox).send_keys(message)
    




