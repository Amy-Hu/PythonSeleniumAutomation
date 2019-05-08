# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import xlsxwriter
import sys
sys.path.append('..')
from TestModel import Functions, MyUnitTest
from TestElements import Common_HomeScreen, Common_SearchScreen, Common_NewAccountDetailsScreen, \
    Common_AccountSummaryScreen, Common_StartAQuoteScreen, GL_CoveragePartsScreen, Common_CommonScreen, \
    Common_BasicPolicyInfoScreen


class CreateGLIndicativeDraft(MyUnitTest.MyTest):

    def test_new_gl_draft(self):
        # Create screenshot excel
        book = xlsxwriter.Workbook('..\MIG_Portal_Automation\TestReports\Create_CA_Issuable_Draft.xlsx')

        # Login Portal
        Functions.login_portal(self.driver)

        # Home page
        homeScreen = Common_HomeScreen.Home(self.driver)
        homeScreen.click_search_icon()

        # Search Screen
        searchScreen = Common_SearchScreen.Search(self.driver)
        searchScreen.input_searchkeyword("4000006373")
        Functions.get_screenshot(self.driver, book, "SearchAccount")
        searchScreen.click_view_button()

        # Account Summary Screen
        accountSummary = Common_AccountSummaryScreen.AccountSummary(self.driver)
        Functions.get_screenshot(self.driver, book, "AccountSummary")
        accountSummary.click_startquote()

        # Start A Quote Screen
        startQuote = Common_StartAQuoteScreen.StartAQuote(self.driver)
        Functions.get_screenshot(self.driver, book, "StartAQuote")
        startQuote.click_generalliability()
        startQuote.click_commercialauto()
        startQuote.click_next_button()

        # Open CA submission
        common = Common_CommonScreen.Common(self.driver)
        common.open_newcreate_submission()

        # Policy Info Screen
        policyInfo = Common_BasicPolicyInfoScreen.BasicPolicyInfo(self.driver)
        submissionnumber = policyInfo.get_submission_number()
        print(submissionnumber)
        Functions.get_screenshot(self.driver, book, "PolicyInfo")

        book.close()








