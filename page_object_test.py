from selenium import webdriver
from pages.todo_page import ToDoPage
import time
import unittest

class TestWithPageObjects(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver')
        self.driver.get('https://todomvc.com/examples/vanillajs/')
        # inicializamos el page object
        self.todo_page = ToDoPage(self.driver)

    def tearDown(self):
        screenshot_file_name = '../screenshots/Screenshot_' + str(time.time()) + '.png'
        self.driver.save_screenshot(screenshot_file_name)
        self.driver.close()
        self.driver.quit()

    def test_crear_nota_numeros(self):
        self.todo_page.add_note('12345')
        self.assertEqual(self.todo_page.get_first_note_text(),'12345')

    def test_crear_nota_texto_largo(self):
        self.todo_page.add_note('Soyunanotitamuyperomuylarga')
        self.assertEqual(self.todo_page.get_first_note_text(),'Soyunanotitamuyperomuylarga')

    def test_crear_nota_caracteres(self):
        self.todo_page.add_note('!@#$%^&*()_)(*&^%$#@)')
        self.assertEqual(self.todo_page.get_first_note_text(),'!@#$%^&*()_)(*&^%$#@)')

    def test_crear_nota_mayusculas(self):
        self.todo_page.add_note('HOLA')
        self.assertEqual(self.todo_page.get_first_note_text(),'HOLA')

    #def test_completar_tarea(self):
    #    self.todo_page.add_note('HOLA')
    #    self.todo_page.complete_task(0)
    #    self.assertTrue(self.todo_page.is_completed_task(0))


if __name__ == '__main__':
    unittest.main()
