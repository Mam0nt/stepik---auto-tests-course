from selenium import webdriver
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_css_selector("[placeholder='Введите имя']")
input1.send_keys('Имя')
input2 = browser.find_element_by_css_selector("[placeholder='Введите фамилию']")
input2.send_keys('Фамилия')
input3 = browser.find_element_by_css_selector("[placeholder='Введите Email']")
input3.send_keys('Email')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
element = browser.find_element_by_id('file')
element.send_keys(file_path)

button = browser.find_element_by_css_selector("[type='submit']")
button.click()
