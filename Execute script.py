from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
link = 'https://suninjuly.github.io/execute_script.html'

def func(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, "input_value").text)
    y = func(x)

    line = browser.find_element(By.ID, "answer")
    line.send_keys(y)
    choose_1 = browser.find_element(By.ID, "robotCheckbox")
    choose_1.click()
    time.sleep(1)
    choose_2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", choose_2)
    choose_2.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(1)




finally:
    time.sleep(5)
    browser.quit()
