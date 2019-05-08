# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class ReferToUnderwriter(BasePage.BaseClass):

    def input_note(self, note):
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='note-body']"))).send_keys(note)

    def click_submit(self):
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='saveNote(newNoteForm)']"))).click()

    def click_cancel(self):
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button tertiary-button-default']"))).click()
        sleep(1)