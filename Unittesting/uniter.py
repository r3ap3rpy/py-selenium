from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class SwitchToAlert(unittest.TestCase):
	def setUp(self):
		global driver
		caps = DesiredCapabilities.FIREFOX
		driver = webdriver.Remote(command_executor='http://redwood:4444/wd/hub',desired_capabilities=caps)
		driver.get('http://r3ap3rpy.pythonanywhere.com/')
		

	def test_Title(self):
		self.assertEqual(driver.title, "R3aperPy")

	def test_Headers(self):
		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(text(),'Home')]"))



	def tearDown(self):
		driver.quit()
	
if __name__ == '__main__':
	unittest.main()