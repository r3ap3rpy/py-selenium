from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep

USER = os.getenv('PYNYWHRUSR')
PASS = os.getenv('PYNYWHRPASS')

driver = webdriver.Chrome()
driver.get('https://www.pythonanywhere.com/')

LoginURL = "//a[@class='login_link']"
UsernameURL = "//input[@id='id_auth-username']"
PasswordURL = "//input[@id='id_auth-password']"
ButtonURL = "//button[@id='id_next']"
WebURL = "//a[@id='id_web_app_link']"
MonthsFromToday = "//input[@value='Run until 3 months from today']"

LoginElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(LoginURL))
LoginElement.click()

UserElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(UsernameURL))
UserElement.send_keys(USER)

PasswordElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PasswordURL))
PasswordElement.send_keys(PASS)

ButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ButtonURL))
ButtonElement.click()

WebElement =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(WebURL))
WebElement.click()

MonthsElement =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(MonthsFromToday))
MonthsElement.click()
sleep(5)

driver.quit()