#script to generate random data for contact us page in mindrisers webpage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest
import random
import string
import re

#validate email
def validate_email(email):
    try:
        if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            return True
        else:
            return False
    except Exception as e:
        print(f"validation error {e}")
        return False
#generate random name
def gName():
    return ''.join(random.choices(string.ascii_lowercase, k=7))
#generate random email
def gEmail():
    domain="gmail.com"
    length=6
    rstring=''.join(random.choices(string.ascii_lowercase, k=length))
    email=rstring+"@"+domain
    return email
#generate phone number
def gPhone():
    return "980"+''.join(random.choices(string.digits, k=7))
#chose random courses
courses=["QA", "MERN", "Cyber security", "Web Devlopment", "SEO"]
def gCourse():
    return random.choice(courses)
#generate random query 
def gQuery():
    words = ["automation", "selenium", "testing", "Python", "quality", "assurance", "script", "developer", "bug", "feature", "performance"]
    query = ' '.join(random.choices(words, k=20)) + "?"
    return query

@pytest.fixture
def browser():
     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
     yield driver
     driver.quit()

@pytest.mark.parametrize("name, email, phone, course, query",[
    (gName(),gEmail(),gPhone(), gCourse(), gQuery() ),
    (gName(),gEmail(),gPhone(), gCourse(), gQuery() )
])

def test_admission(browser, name, email, phone, course, query):
    #get url
    url="https://www.mindrisers.com.np/contact-us"
    browser.get(url)
    browser.maximize_window()
    browser.execute_script("window.scrollBy(0, 800);")
   #finding input fields
    Name_field=browser.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
    Email_field=browser.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
    phone_field=browser.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
    subject_field=browser.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
    queries_field=browser.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))
    #clear the field 
    Name_field.clear()
    Email_field.clear()
    phone_field.clear()
    subject_field.clear()
    queries_field.clear()
    #send the values
    Name_field.send_keys(name)
    Email_field.send_keys(email)
    phone_field.send_keys(phone)
    subject_field.send_keys(course)
    queries_field.send_keys(query)
    time.sleep(4)


    
