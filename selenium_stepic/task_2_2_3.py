from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);")

    option_check = browser.find_element_by_id("robotCheckbox")
    option_check.click()
    option_radio = browser.find_element_by_id("robotsRule")
    option_radio.click()

    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
