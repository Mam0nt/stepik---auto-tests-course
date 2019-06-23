from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('num1')
x = int(x_element.text)
print (x)

y_element = browser.find_element_by_id('num2')
y = int(y_element.text)
print (y)

z = str(x + y)
print (z)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)

time.sleep(1)

button = browser.find_element_by_tag_name('button')
button.click()