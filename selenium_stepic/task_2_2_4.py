from selenium import webdriver
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys("First name")
    input2 = browser.find_element_by_xpath('//input[@name="lastname"]')
    input2.send_keys("Last name")
    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys("Email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    send1 = browser.find_element_by_xpath('//input[@type="file"]')
    send1.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:

    time.sleep(5)
    browser.quit()
