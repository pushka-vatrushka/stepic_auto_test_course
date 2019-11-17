from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    wait = WebDriverWait(browser, 20)
    money = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_tag_name("button")
    button.click()

    input1 = browser.find_element_by_id("input_value")
    y = calc(input1.text)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)

    button2 = browser.find_element_by_tag_name("button#solve")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
