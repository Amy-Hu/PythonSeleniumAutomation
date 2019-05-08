# -*- coding: utf-8 -*-
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
# from datetime import datetime
from time import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from openpyxl import load_workbook
import xlsxwriter
import unittest, time
from unittest import defaultTestLoader
import sys
case_path = './TestCases'

def get_allcase():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_Create_GL_Issuable_Issued.py")
    #discover = unittest.defaultTestLoader.discover(case_path, pattern="test_Create_NewAccount.py")
    #discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    testsuite = unittest.TestSuite()
    testsuite.addTest(discover)
    return testsuite

if __name__ == "__main__":
    #testsuit = unittest.TestSuite()
    #testsuit.addTest(Create_NewAccount.CreateNewAccount("test_new_account"))
    now = time.strftime("%Y%m%d_%H%M%S")
    filename = './TestReports/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='automation report', description='case execution status')
    runner.run(get_allcase())
    fp.close()


