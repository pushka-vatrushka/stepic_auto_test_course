from selenium import webdriver
import time

try:
	link1 = "http://suninjuly.github.io/registration1.html"
	link2 = "http://suninjuly.github.io/registration2.html"
	#использую браузер Firefox, для Google Chrome заменить на webdriver.Chrome()
	browser = webdriver.Chrome()
	browser.get(link2) #для проверки первого задания заменить на link1
	#заполнение обязательных полей
	text1 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input")
	text1.send_keys("Alla")
	text2 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input")
	text2.send_keys("Gavrilova")
	text3 = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input")
	text3.send_keys("test@test.ru")
	time.sleep(10)
	 # отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
	# проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)
	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text
	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	# ожидание, чтобы визуально оценить результаты прохождения скрипта
	time.sleep(3)
	# закрываем браузер после всех манипуляций
	browser.quit()
