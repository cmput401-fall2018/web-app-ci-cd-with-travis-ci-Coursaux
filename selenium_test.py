from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def test_home():
    driver = webdriver.Chrome()
    driver.get("http://204.209.76.170:8000")
    elem = driver.find_element_by_id("name")
    assert elem != None
    elem = driver.find_element_by_id("about")
    assert elem != None
    elem = driver.find_element_by_id("education")
    assert elem != None
    elem = driver.find_element_by_id("skills")
    assert elem != None
    elem = driver.find_element_by_id("work")
    assert elem != None
    elem = driver.find_element_by_id("contact")
    assert elem != None

test_home()
