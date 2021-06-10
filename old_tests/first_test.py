from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class OurFirstTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('../config/chromedriver')
		self.driver.get('https://todomvc.com/examples/vanillajs/')

	def tearDown(self):
		screenshot_file_name = '../screenshots/Screenshot_' + str(time.time()) + '.png'
		self.driver.save_screenshot(screenshot_file_name)
		self.driver.close()
		self.driver.quit()

	def test_crear_nota(self):
		search_input = self.driver.find_element_by_css_selector('.new-todo')
		search_input.click()
		search_input.send_keys('Soy una notita')
		search_input.send_keys(Keys.ENTER)
		first_note_text = self.driver.find_element_by_css_selector('.view > label')
		self.assertEqual(first_note_text.text,'Soy una notita')

	def test_crear_dos_notas(self):
		search_input = self.driver.find_element_by_css_selector('.new-todo')
		search_input.click()
		search_input.send_keys('Soy una notita')
		search_input.send_keys(Keys.ENTER)
		search_input.click()
		search_input.send_keys('Soy otra notita')
		search_input.send_keys(Keys.ENTER)
		first_note_text = self.driver.find_element_by_css_selector('.view > label')
		self.assertTrue(first_note_text.text == 'Soy una notita')



if __name__ == '__main__':
	unittest.main()
