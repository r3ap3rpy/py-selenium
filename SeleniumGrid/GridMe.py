from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep

USER = os.getenv('PYNYWHRUSR')
PASS = os.getenv('PYNYWHRPASS')

caps = DesiredCapabilities.FIREFOX

driver = webdriver.Remote(command_executor='http://redwood:4444/wd/hub',desired_capabilities=caps)
driver.get('https://www.pythonanywhere.com/')

LoginURL = "//a[@class='login_link']"
UsernameURL = "//input[@id='id_auth-username']"
PasswordURL = "//input[@id='id_auth-password']"
ButtonURL = "//button[@id='id_next']"
WebURL = "//a[@id='id_web_app_link']"
MonthsFromToday = "//input[@value='Run until 3 months from today']"

print('Looking for the login element!')
LoginElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(LoginURL))
LoginElement.click()

print('Looking for the username field!')
UserElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(UsernameURL))
UserElement.send_keys(USER)

print('Looking for the password field!')
PasswordElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PasswordURL))
PasswordElement.send_keys(PASS)


print('Looking for the login button!')
ButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ButtonURL))
ButtonElement.click()

print('Looking for the web url!')
WebElement =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(WebURL))
WebElement.click()

print('Looking for the renew element!')
MonthsElement =  WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(MonthsFromToday))
MonthsElement.click()
sleep(5)

driver.quit()