#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class StartAQuote(BasePage.BaseClass):
  
    def click_indicative(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located((By.ID, "radio_7"))).click()
    
    def click_generalliability(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "mig-icon-bandaid"))).click()

    def click_commercialauto(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//a[@ng-data='auto']"))).click()

    def click_crime(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='choose-lob']/div[3]/div[4]/a"))).click()

    def click_umb(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//a[@ng-data='umb']"))).click()

    def click_workscomp(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "mig-icon-wc"))).click()

    def click_commercialpackage(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH,"//a[@ng-data='cpp']"))).click()

    def click_businessowners(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH,"//a[@ng-data='bop']"))).click()

    def click_commercialproperty(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//a[@ng-data='commProperty']"))).click()

    def click_inlandmarine(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, By.XPATH,"//a[@ng-data='im']"))).click()

    def click_next_button(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='submitSelectedProducts(newSubmissionForm)']"))).click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")