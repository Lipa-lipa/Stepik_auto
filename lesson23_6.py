from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    
    # Нажать на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    time.sleep(0)
    
    #Переключиться на новую вкладку
    new_window = browser.window_handles[1] #получили массив имен вкладок
    browser.switch_to.window(new_window) #переключились на нужную вкладку
    
    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    time.sleep(0)
    
    # Нажать на Submit
    button2 = browser.find_element(By.CLASS_NAME, "btn")
    button2.click()
    time.sleep(3)
   
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
