# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class QuoteSummary(BasePage.BaseClass):

    def get_quote_status(self):
        sleep(1)
        return WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='wizard-sidebar-steps']/div/small[1]"))).text

    def click_makeissuablequote(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button back-button xs-smaller']"))).click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def click_gotoerror(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='nbs-link']"))).click()
        sleep(5)

    def click_folderror(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-chevron-up']"))).click()
        sleep(1)
