# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class CGL(BasePage.BaseClass):

    def click_next_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='nbs-button orange-button next-button']"))).click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        sleep(1)

    def click_classcodes_tab(self):
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        gltab = self.driver.find_elements_by_xpath("//a[@ng-click='switchTab(tab)']")
        gltab[1].click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def input_classcode(self, classcode):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='ClassCode']"))).send_keys(classcode)
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//span[@ng-click='clickOnSuggestionItem(item)']"))).click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def input_annualbasis(self, annualbasis):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-model='premABDisplayValue.value']"))).send_keys(annualbasis)
        self.driver.find_element_by_xpath("//input[@ng-model='premABDisplayValue.value']").send_keys(Keys.TAB)
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def click_supplementalinfo_tab(self):
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        gltab = self.driver.find_elements_by_xpath("//a[@ng-click='switchTab(tab)']")
        gltab[6].click()
        if Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']"):
            Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")

    def answer_all_questions(self):
        questions = self.driver.find_elements_by_xpath("//md-radio-button[@aria-label='No']")
        js = "var q=document.documentElement.scrollTop=100"
        self.driver.execute_script(js)
        questions[0].click()
        self.driver.execute_script(js)
        questions[1].click()
        js = "var q=document.documentElement.scrollTop=200"
        self.driver.execute_script(js)
        questions[2].click()
        js = "var q=document.documentElement.scrollTop=300"
        self.driver.execute_script(js)
        questions[3].click()
        js = "var q=document.documentElement.scrollTop=400"
        self.driver.execute_script(js)
        questions[4].click()
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        questions[5].click()
        js = "var q=document.documentElement.scrollTop=600"
        self.driver.execute_script(js)
        questions[6].click()
        js = "var q=document.documentElement.scrollTop=700"
        self.driver.execute_script(js)
        questions[7].click()
        js = "var q=document.documentElement.scrollTop=800"
        self.driver.execute_script(js)
        questions[8].click()
        js = "var q=document.documentElement.scrollTop=850"
        self.driver.execute_script(js)
        questions[9].click()
        js = "var q=document.documentElement.scrollTop=900"
        self.driver.execute_script(js)
        questions[10].click()
        js = "var q=document.documentElement.scrollTop=950"
        self.driver.execute_script(js)
        questions[11].click()
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        questions[12].click()
        js = "var q=document.documentElement.scrollTop=1020"
        self.driver.execute_script(js)
        questions[13].click()
        js = "var q=document.documentElement.scrollTop=1100"
        self.driver.execute_script(js)
        questions[14].click()
        js = "var q=document.documentElement.scrollTop=1180"
        self.driver.execute_script(js)
        questions[15].click()
        js = "var q=document.documentElement.scrollTop=1260"
        self.driver.execute_script(js)
        questions[16].click()
        js = "var q=document.documentElement.scrollTop=1340"
        self.driver.execute_script(js)
        questions[17].click()
        js = "var q=document.documentElement.scrollTop=1420"
        self.driver.execute_script(js)
        questions[18].click()
        js = "var q=document.documentElement.scrollTop=1500"
        self.driver.execute_script(js)
        questions[19].click()
        js = "var q=document.documentElement.scrollTop=1580"
        self.driver.execute_script(js)
        questions[20].click()
        js = "var q=document.documentElement.scrollTop=1660"
        self.driver.execute_script(js)
        questions[21].click()
        js = "var q=document.documentElement.scrollTop=1740"
        self.driver.execute_script(js)
        questions[22].click()
        js = "var q=document.documentElement.scrollTop=1820"
        self.driver.execute_script(js)
        questions[23].click()
        js = "var q=document.documentElement.scrollTop=1900"
        self.driver.execute_script(js)
        questions[24].click()
        js = "var q=document.documentElement.scrollTop=1880"
        self.driver.execute_script(js)
        questions[25].click()