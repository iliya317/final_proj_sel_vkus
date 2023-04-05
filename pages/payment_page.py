from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


# login_standard_user = 'standard_user'
# password_all = 'secret_sauce'
# g = Service('chromedriver.exe')
# driver = webdriver.Chrome(service='chromedriver.exe')

class Payment(Base):


    def __init__(self,driver):

        self.driver = driver

        # Locators

        self.button_finish = '//button[@id="finish"]'   

        
    # Getters


    
    def get_button_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.button_finish)))



    # Actions


    def click_button_finish(self):
        self.get_button_finish().click()
        print('continue pressed')


    
    # Actions

    def finish_payment(self):

        self.click_button_finish()
        
