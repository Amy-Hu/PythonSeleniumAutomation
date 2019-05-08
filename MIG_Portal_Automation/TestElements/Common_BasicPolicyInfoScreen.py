# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class BasicPolicyInfo(BasePage.BaseClass):

    def get_submission_number(self):
        #Functions.wait_element_display(self.driver, By.XPATH, "//select[@ng-model='draftDataDTOObj.accountHolder.value.accountOrgType']")
        return WebDriverWait(self.driver, 15, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='wizard nbs']/div[1]/div[2]/div[3]/div/div/div/small[2]"))).text

    def select_organizationtype(self, organization):
        #Functions.wait_element_display(self.driver, By.XPATH, "//select[@ng-model='draftDataDTOObj.accountHolder.value.accountOrgType']")
        Select(self.driver.find_element_by_xpath("//select[@ng-model='draftDataDTOObj.accountHolder.value.accountOrgType']")).select_by_visible_text(organization)

    def input_yearbusinessstarted(self, year):
        #target = self.driver.find_element(By.XPATH, "//span[@mig-tooltip='platform.tooltip.yearBusinessStarted']/div/div/ng-transclude/md-input-container/input")
        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
        yearbusinessstarted = WebDriverWait(self.driver, 15, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//span[@mig-tooltip='platform.tooltip.yearBusinessStarted']/div/div/ng-transclude/md-input-container/input")))
        if yearbusinessstarted.text != "":
            yearbusinessstarted.clear()
            sleep(1)
            yearbusinessstarted.send_keys(year)
        else:
            yearbusinessstarted.send_keys(year)

    def input_descriptionofbusiness(self, description):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//span[@mig-tooltip='platform.tooltip.businessOpsDescription']/div/div/ng-transclude/md-input-container/input"))).send_keys(description)

    def input_fein(self, fein):
        fein = WebDriverWait(self.driver, 15, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@ng-placeholder='##-########']")))
        if fein.text != "":
            fein.clear()
            sleep(1)
            fein.send_keys(fein)
        else:
            fein.send_keys(fein)

    def click_next_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button next-button']"))).click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")