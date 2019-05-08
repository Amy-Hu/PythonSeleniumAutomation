# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class PolicyReview(BasePage.BaseClass):

    def click_quote_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button next-button']"))).click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")