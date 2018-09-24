from time import sleep
from selenium import webdriver


driver = webdriver.Edge()

driver.get('https://www.google.com/')


sleep(5)

driver.quit()