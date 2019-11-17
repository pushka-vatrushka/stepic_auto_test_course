from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    kick_picture = browser.find_element_by_id("treasure")
    x_element = kick_picture.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(y)

    option_check = browser.find_element_by_id("robotCheckbox")
    option_check.click()
    option_radio = browser.find_element_by_id("robotsRule")
    option_radio.click()

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
