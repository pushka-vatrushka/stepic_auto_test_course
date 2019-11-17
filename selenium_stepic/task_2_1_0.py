from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("div.container span.nowrap#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_xpath('//input[@class="form-control"]')
    input1.send_keys(y)

    # robots_radio = browser.find_element_by_id("robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None

    option_check = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option_check.click()
    option_radio = browser.find_element_by_css_selector("[for='robotsRule']")
    option_radio.click()

    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
