from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://vk.com/im?peers=c21&sel=154435271"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_id('email')
input1.send_keys("89969319528")
input2 = browser.find_element_by_id('pass')
input2.send_keys("irpapenis")
button = browser.find_element_by_id("login_button")
button.click()
time.sleep(1)
input3 = browser.find_element_by_class_name('im_editable')
input3.send_keys("Доброе утро, моя зайка***\n")


