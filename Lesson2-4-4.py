from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	# говорим WebDriver ждать все элементы в течение 5 секунд
	browser.implicitly_wait(5)

	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	button = WebDriverWait(browser, 12).until(
	        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

	button = browser.find_element_by_id("book")
	button.click()

	element1 = browser.find_element_by_id('input_value')
	x = element1.text
	y = calc(x)

	input1 = browser.find_element_by_css_selector('#answer')
	input1.send_keys(y)
  # Отправляем заполненную форму
	button1 = browser.find_element_by_id('solve')
	button1.click()

    # находим элемент, содержащий текст
	welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # успеваем скопировать код за 30 секунд
	time.sleep(5)
    # закрываем браузер после всех манипуляций
	browser.quit()