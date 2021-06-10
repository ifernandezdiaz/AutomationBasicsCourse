from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class TestWithoutPageObjects(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver')
        self.driver.get('https://todomvc.com/examples/vanillajs/')

    def tearDown(self):
        screenshot_file_name = '../screenshots/Screenshot_' + str(time.time()) + '.png'
        self.driver.save_screenshot(screenshot_file_name)
        self.driver.close()
        self.driver.quit()

    def test_crear_nota_numeros(self):
        search_input = self.driver.find_element_by_css_selector('.new-todo')
        search_input.click()
        search_input.send_keys('12345')
        search_input.send_keys(Keys.ENTER)
        first_note_text = self.driver.find_element_by_css_selector('.view > label')
        self.assertEqual(first_note_text.text,'12345')

    def test_crear_nota_texto_largo(self):
        search_input = self.driver.find_element_by_css_selector('.new-todo')
        search_input.click()
        search_input.send_keys('Soyunanotitamuyperomuylarga')
        search_input.send_keys(Keys.ENTER)
        first_note_text = self.driver.find_element_by_css_selector('.view > label')
        self.assertEqual(first_note_text.text,'Soyunanotitamuyperomuylarga')

    def test_crear_nota_caracteres(self):
        search_input = self.driver.find_element_by_css_selector('.new-todo')
        search_input.click()
        search_input.send_keys('!@#$%^&*()_)(*&^%$#@)')
        search_input.send_keys(Keys.ENTER)
        first_note_text = self.driver.find_element_by_css_selector('.view > label')
        self.assertEqual(first_note_text.text,'!@#$%^&*()_)(*&^%$#@)')

    def test_crear_nota_mayusculas(self):
        search_input = self.driver.find_element_by_css_selector('.new-todo')
        search_input.click()
        search_input.send_keys('HOLA')
        search_input.send_keys(Keys.ENTER)
        first_note_text = self.driver.find_element_by_css_selector('.view > label')
        self.assertEqual(first_note_text.text, 'HOLA')


if __name__ == '__main__':
    unittest.main()
