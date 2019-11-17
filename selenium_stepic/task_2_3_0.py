from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_tag_name("button")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    input1 = browser.find_element_by_id("input_value")
    y = calc(input1.text)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)

    button2 = browser.find_element_by_tag_name("button")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
