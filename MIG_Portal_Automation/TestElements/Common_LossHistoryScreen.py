# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class LossHistory(BasePage.BaseClass):

    def select_lengthofpriorlosshistory(self, value):
        lengthofpriorlosshistory = self.driver.find_element(By.XPATH, "//select[@gw-pl-select='lossHistoryDTO.value.lengthOfPriorLossHistory']")
        Select(lengthofpriorlosshistory).select_by_visible_text(value)

    def select_priorlosshistory(self, value):
        Select(WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//select[@gw-pl-select='lossHistoryDTO.value.priorLossHistory']")))).select_by_visible_text(value)

    def click_next_button(self):
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button next-button']"))).click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")