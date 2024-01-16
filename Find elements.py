from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element, fill in zip(elements, ["Ivan", "Petrov", "Smolensk", "Russia"]):
        element.send_keys(fill)

    button = browser.find_element(By.XPATH, "//body//div//form//div[6]//button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


