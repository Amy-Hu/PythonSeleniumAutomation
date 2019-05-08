from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions


class Common(BasePage.BaseClass):

    def open_newcreate_submission(self):
        AllQuotes = WebDriverWait(self.driver, 30, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='wizard-sidebar-policies']")))
        lis = AllQuotes.find_elements_by_xpath('div')
        lis[-1].click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        sleep(1)

    def click_feedback_button(self):
        WebDriverWait(self.driver, 30, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='mcxFeedback']"))).click()



