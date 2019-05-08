from selenium import webdriver
import unittest
from openpyxl import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import sys
#sys.path.append(r'C:\AmyPersonal\MIG_Portal_Automation\SupportFunctions')
#import Functions

class MyTest(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()