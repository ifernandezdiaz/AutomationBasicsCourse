from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ToDoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver);
        self.search_input = (By.CSS_SELECTOR, '.new-todo')
        self.notes = (By.CSS_SELECTOR, '.todo-list > li')
        self.toggle_task_status = (By.CSS_SELECTOR, '.toggle')
        self.completed_task = 'completed'

    def add_note(self,text_note):
        self.type_text(text_note,*self.search_input)

    def get_task(self, pos):
        return self.find_elements(*self.notes)[pos]

    def get_first_note_text(self):
        return self.get_task(0).text
