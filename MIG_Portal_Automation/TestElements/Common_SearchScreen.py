from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import *
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class Search(BasePage.BaseClass):

    def click_createanewone_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//div[@ng-if='allowAccountCreation']/a"))).click()
 
    def input_searchkeyword(self, keyword):
        sleep(2)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))).send_keys(keyword)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER)
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def click_view_button(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='secondary-button desktop-only medium']"))).click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        if(Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")



