from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.common.exceptions import TimeoutException




class cartpage(Base):


    def __init__(self,driver):

        self.driver = driver

        # Locators
        self.name_locator = '//input[@name="UNAME"]'
        self.phone_locator = '//input[@name="UPHONE"]'
        self.email_locator = '//input[@name="UEMAIL"]'
        self.therminal_payment = "//input[@data-pay-way= '3']"
        self.flat_locator = '//input[@name="FLAT"]'
        self.submit = "//button[@class='VV23_Order_Submit_Button VV_Button _desktop-lg _tablet-lg _mobile-lg _block js-order-btn-submit js-hide-float-button']"
        self.autorization_button_no = "//a[@class='VV_Button _tertiary _block _desktop-lg _tablet-lg _mobile-md js-order-nonauthed-go']"

    # Getters

    def get_name_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH ,  self.name_locator)))
    
    def get_phone_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH ,  self.phone_locator)))
    
    def get_email_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH ,  self.email_locator)))
    
    def get_therminal_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH ,  self.therminal_payment)))
    
    def get_flat_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH ,  self.flat_locator)))
    
    def get_submit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH ,  self.submit)))
    
    def get_allert_autorization(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH , self.autorization_button_no)))
        except  TimeoutException: 
            return 1
    



    # Actions

    def post_name_locator(self,name):
        self.get_name_locator().send_keys(name)
    
    def post_phone_locator(self,phone):
        self.get_phone_locator().send_keys(phone)

    def post_email_locator(self, email):
        self.get_email_locator().send_keys(email)


    def click_therminal_payment(self):
        self.driver.execute_script("arguments[0].click();", self.get_therminal_payment())


    def post_flat_locator(self, flat):
        body = self.get_flat_locator()
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(flat)


    def click_submit(self):
        self.get_submit().click()

    def pass_allert_autorization(self):
        fun = self.get_allert_autorization()
        if fun == 1:
            return 1 
        else:
            return fun.click()







