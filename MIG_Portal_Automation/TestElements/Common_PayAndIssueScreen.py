from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class PayAndIssue(BasePage.BaseClass):

    def click_payandissue_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button next-button']"))).click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def input_emaiaddress(self, emailaddress):
        pass
        #target = self.driver.find_element(By.XPATH, "//input[@name='Email Address']")
        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
        #ActionChains(self.driver).move_to_element(target).click().perform()

    def select_cashfullpay(self):
        paymentplan = self.driver.find_elements_by_xpath("//input[@ng-click='selectPlan(item.billingID)']")
        self.driver.execute_script("arguments[0].scrollIntoView();", paymentplan[0])
        ActionChains(self.driver).move_to_element(paymentplan[0]).click().perform()

    def select_mailcheck(self):
        sleep(1)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        paymentmethod = self.driver.find_elements_by_xpath("//button[@class='square btn-icon-button']")
        self.driver.execute_script("arguments[0].scrollIntoView();", paymentmethod[3])
        ActionChains(self.driver).move_to_element(paymentmethod[3]).click().perform()


