from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


class OurFirstTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../config/chromedriver')
        self.driver.get('http://uitestingplayground.com/clientdelay')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_chequear_wait(self):
        button = self.driver.find_element(By.ID, 'ajaxButton')
        button.click()
        wait = WebDriverWait(self.driver, 20)
        message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.bg-success')))
        assert message.text == 'Data calculated on the client side.'


if __name__ == '__main__':
    unittest.main()
