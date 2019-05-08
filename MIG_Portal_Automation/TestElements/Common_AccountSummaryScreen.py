#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class AccountSummary(BasePage.BaseClass):
  
    def click_startquote(self):
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='row align-middle']/div[2]/div/div[2]/button"))).click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def get_accountstatus(self):
        sleep(1)
        return WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='navyblue-light-text--large']"))).text
 
    def get_accountnumber(self):
        sleep(1)
        return WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='light-blue-text--lg']"))).text

    