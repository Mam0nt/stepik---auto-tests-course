from selenium import webdriver
import time
browser = webdriver.Chrome()

email = input("Введите email\t>> ")
password = input("Введите пароль\t>> ")

browser.get("https://stepik.org/course/575/promo?auth=login")
time.sleep(3)
def click(s):
    browser.find_element_by_css_selector(s).click()
def clickxpath(s):
    browser.find_element_by_xpath(s).click()
def send(s,keys):
    browser.find_element_by_css_selector(s).send_keys(keys)

send('[name = "login"]', email)
send('[name = "password"]', password)
click(".sign-form__btn")
time.sleep(1)

s = ['//*[contains(text(), "работа с выпадающими списками")]',
'//*[contains(text(), "переключение между окнами браузера")]',
'//*[contains(text(), "настройка запуска определенного набора тестов")]',
'//*[contains(text(), "работа с отчётами для упавших автотестов")]',
'//*[contains(text(), "как получать значения атрибутов html-элементов")]',
'//*[contains(text(), "работа с явными и неявными ожиданиями")]',]
def nl(n):
    return (10 - len(bin(n))) * "0" + bin(n)[2:]

def c(n = 0):
    while True:
        n += 1
        print(n)
        es = []
        c = nl(n)
        for i in range(6):
            if c[i] == "1":
                es.append(s[i])
        for i in es:
            clickxpath(i)
            time.sleep(0.05)
        click(".submit-submission")
        time.sleep(1.5)
        click(".again-btn")
        time.sleep(1.5)
        if n > 255:
            return "!"

def ss():
    browser.get("https://stepik.org/lesson/236205/step/2?unit=208637")
    time.sleep(4)
    browser.execute_script("window.scrollBy(0, 300);")
    c()
    
ss()