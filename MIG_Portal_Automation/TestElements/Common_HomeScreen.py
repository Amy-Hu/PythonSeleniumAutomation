from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('..')
from TestModel import BasePage, Functions

class Home(BasePage.BaseClass):

    def click_search_icon(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "search-icon"))).click()
      
  
   
        
   