# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class CoverageParts(BasePage.BaseClass):

    def get_quote_status(self):
        sleep(1)
        return WebDriverWait(self.driver, 15, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='wizard-sidebar-steps']/div/small[1]"))).text

    def click_commercialgeneralliability(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, "//i[@class='PremisesOperationsAndProductsCompletedOperations']"))).click()

    def click_epli(self):
        #target = self.driver.find_element(By.XPATH, "//i[@class='EPLI_Ext']")
        #self.driver.execute_script("arguments[0].scrollIntoView();", target)
        #ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, "//i[@class='EPLI_Ext']")).click().perform()
        #self.driver.execute_script("scroll(0,2500)")
        sleep(1)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='EPLI_Ext']"))).click()

    def click_cyberliability(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='CyberLiability']"))).click()

    def click_next_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button next-button']"))).click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")