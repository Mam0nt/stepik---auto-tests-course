from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input_name = browser.find_element_by_css_selector('.first_block .form-control.first')
input_name.send_keys('some_name')
input_second_name = browser.find_element_by_css_selector('.first_block .form-control.second')
input_second_name.send_keys('some_second_name')
input_email = browser.find_element_by_css_selector('.first_block .form-control.third')
input_email.send_keys('some@email.com')
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text