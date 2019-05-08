from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class PC(BasePage.BaseClass):

    def search_submission(self, submission):
        sleep(2)
        policy_drop_down = self.driver.find_element(By.ID, "TabBar:PolicyTab")
        ActionChains(self.driver).move_to_element_with_offset(to_element=policy_drop_down, xoffset=80, yoffset=10).click().perform()
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='TabBar:PolicyTab:PolicyTab_SubmissionNumberSearchItem-inputEl']"))).send_keys(submission)
        self.driver.find_element_by_xpath("//input[@id='TabBar:PolicyTab:PolicyTab_SubmissionNumberSearchItem-inputEl']").send_keys(Keys.ENTER)
        sleep(3)

    def click_riskanalysis(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='SubmissionWizard:0-body']/div/table/tbody/tr[11]/td/div/span"))).click()
        sleep(2)

    def checkon_uwissues(self):
        uwissue = self.driver.find_elements_by_xpath("//img[@class='x-grid-checkcolumn']")
        for i in uwissue:
            i.click()

    def click_approve(self):
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@id='SubmissionWizard:Job_RiskAnalysisScreen:RiskAnalysisCV:RiskEvaluationPanelSet:Approve-btnInnerEl']"))).click()

    def click_ok(self):
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@id='RiskApprovalDetailsPopup:Update-btnInnerEl']"))).click()

    def uncheck_hide(self):
        sleep(4)
        hidecheckbox = self.driver.find_element(By.XPATH, "//img[@class='x-grid-checkcolumn x-grid-checkcolumn-checked']")
        ActionChains(self.driver).move_to_element_with_offset(to_element=hidecheckbox, xoffset=3,
                                                              yoffset=3).click().perform()
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[@class='x-grid-checkcolumn x-grid-checkcolumn-checked']"))).click()
        sleep(2)

    def click_next(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@id='SubmissionWizard:Next-btnInnerEl']"))).click()
