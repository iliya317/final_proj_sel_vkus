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

        self.button_good = "//a[@id='js-lk-modal-alert-btn-text']"
        self.button_cancel_allert = "//button[@class='VV_Button _block _desktop-md _tablet-md _mobile-md']"
        self.button_ok = '//a[@data-dismiss="modal"]'

    def button_cancel_order(self, data):
        return f"//a[@data-id='{data}']"

        
    # Getters


    
    def get_button_good(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.button_good)))
    
    def get_button_cancel_order(self,data):
        return self.driver.find_element(By.XPATH , self.button_cancel_order(data))
    
    def get_button_cancel_allert(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.button_cancel_allert)))
    
    def get_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.button_ok)))



    # Actions


    def click_button_good(self):
        self.get_button_good().click()
        

    def click_button_cancel_order(self):
        order_id = Base(self.driver)
        url = order_id.get_current_url()
        self.driver.execute_script("arguments[0].click();", self.get_button_cancel_order(url[(url.find('=')+1): url.find('&')]))
        

    def click_button_ok(self):
        self.get_button_ok().click()
        
    def click_button_cancel_allert(self):
        self.get_button_cancel_allert().click()

    


