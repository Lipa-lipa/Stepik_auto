from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(2)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
