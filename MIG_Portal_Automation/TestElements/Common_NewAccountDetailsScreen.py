from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class NewAccount(BasePage.BaseClass):

    def input_company(self, company):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.ID, "inputCtrl0"))).click()
        ActionChains(self.driver).click(self.driver.find_element_by_id("inputCtrl0")).send_keys(company).perform()
        sleep(1)

    def click_currentcustomer_no(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.ID, "No_"))).click()

    def input_address(self, address):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@ng-model='addressOwner.addressLine1.value']"))).send_keys(address)

    def input_postalcode(self, postalcode):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@label='Postal Code']"))).send_keys(postalcode)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@label='Postal Code']").send_keys(Keys.TAB)
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='address']/div/a"))).click()
        sleep(1)

    def input_city(self, city):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='City']"))).send_keys(city)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@aria-label='City']").send_keys(Keys.TAB)
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='address']/div/a"))).click()
        sleep(1)

    def select_state(self, state):
        Select(self.driver.find_element_by_xpath("//select[@ng-placeholder='State']")).select_by_visible_text(state)
        sleep(1)
        self.driver.find_element_by_xpath("//select[@ng-placeholder='State']").send_keys(Keys.TAB)
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='address']/div/a"))).click()
        sleep(1)

    def input_county(self, county):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='County']"))).send_keys(county)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@aria-label='County']").send_keys(Keys.TAB)
        sleep(1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='address']/div/a"))).click()
        sleep(1)

    def select_addresstype(self):
        Select(self.driver.find_element_by_css_selector(".gw-pl-select")).select_by_index(2)
        #WebDriverWait(self.driver,15,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".gw-pl-select"))).select_by_index(2)

    def input_officephone(self, phone):
        ActionChains(self.driver).click(self.driver.find_element_by_xpath("//input[@ng-init='validatePhoneNumber()']")).send_keys(phone).perform()

    def select_contactmethod(self):
        Select(self.driver.find_element_by_xpath("//select[@ng-model='accountInfoView.value.communication.code']")).select_by_index(2)

    def click_next_button(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")
        Functions.wait_element_not_visible(self.driver, By.XPATH, "//h3[@class ='modal-title']")


        