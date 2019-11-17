from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    kick_x = browser.find_element_by_css_selector("#num1")
    x = int(kick_x.text)
    kick_y = browser.find_element_by_css_selector("#num2")
    y = int(kick_y.text)
    z = x + y

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
