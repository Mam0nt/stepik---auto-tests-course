from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

valuex = browser.find_element_by_id('treasure')
x = int(valuex.get_attribute('valuex'))
print ('x = ', x)
y = calc(x)
print ('y = ', y)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)
option1 = browser.find_element_by_css_selector("[type='checkbox']")
option1.click()
option2 = browser.find_element_by_id("robotsRule")
option2.click()
time.sleep(1)
button = browser.find_element_by_css_selector("[type='submit']")
button.click()
