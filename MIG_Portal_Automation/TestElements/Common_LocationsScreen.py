# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class Locations(BasePage.BaseClass):

    def click_addlocation_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='chooseLocationToCreate()']"))).click()

    def click_next_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button next-button']"))).click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
