from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math

  
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_elements = browser.find_element(By.XPATH, "//h2/span[@id='num1']")
    a = a_elements.text
    b_elements = browser.find_element(By.XPATH, "//h2/span[@id='num2']")
    b = b_elements.text
    x = str(int(a)+int(b))
    browser.find_element(By.XPATH, "//div/select[@id='dropdown']").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x)
    opt3 = browser.find_element(By.XPATH, "//button[@class='btn btn-default']").click()
    
finally:
    time.sleep(5)
    browser.quit()