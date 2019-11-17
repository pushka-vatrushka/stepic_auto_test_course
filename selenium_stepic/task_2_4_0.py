from selenium import webdriver
import time

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(link)
    button1 = browser.find_element_by_id("button")
    button1.click()

finally:
    time.sleep(5)
    browser.quit()
