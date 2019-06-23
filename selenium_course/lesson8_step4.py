from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button1 = browser.find_element_by_css_selector("[type='submit']")
button1.click()

alert = browser.switch_to.alert
alert.accept()

valuex = browser.find_element_by_id('input_value')
x = int(valuex.text)

y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button2 = browser.find_element_by_css_selector("[type='submit']")
button2.click()