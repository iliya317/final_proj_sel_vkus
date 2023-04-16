from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.common.exceptions import TimeoutException


# login_standard_user = 'standard_user'
# password_all = 'secret_sauce'
# g = Service('chromedriver.exe')
# driver = webdriver.Chrome(service='chromedriver.exe')

class finish(Base):


    def __init__(self,driver):

        self.driver = driver

        # Locators
    
        self.adress = "//textarea[@class= 'VV_Input__Input js-vv-control__input js-delivery__shopselect--form-address']"
        self.clean_adress_button =  "//button[@class= 'VV_Input__Clear js-address-clear']"
        self.confirm_adress_button = '//a[@class = "_delivery VV_Button _block js-delivery__service-select Delivery__ShopSelect--map_delivery_block"]'
        self.suggest_address = '//div[@class="DeliverySearchInput__suggestAddress "]'
        self.clear_button = '//button[@class="VV_Button _desktop-lg _tablet-lg _mobile-md js-delivery__shopselect-terms-accept _block"]'
        self.deliver_here_button = "//div[@class='Delivery__ShopSelectModal__AddressMapDelivHere js-delivery__shopselect--search-map-deliv-here']"
        self.allert_no_stocks = "//div[@id='js-lk-modal-alert-text']"
        self.allert_no_stock_button = "//a[@id='js-lk-modal-alert-btn-text']"
        

        
    # Getters
    def get_adress_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.adress)))
    
    def get_clean_adress(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.clean_adress_button)))
    
    def get_confirm_adress(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.confirm_adress_button)))
    
    def get_suggest_adress(self):
        self.driver.implicitly_wait(5)
        return self.driver.find_element(By.XPATH, self.suggest_address) #WebDriverWait(self.driver, 30).until(EC.title_contains('Москва, Сумской проезд, влд. 9Б')((By.XPATH , self.suggest_address)))
    
    def get_clear_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.clear_button)))
    
    def get_deliver_here(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.deliver_here_button)))
    
    def get_allert_no_stocks(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH , self.allert_no_stocks)))
        except  TimeoutException: 
            return 1
    
    def get_allert_no_stocks_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.allert_no_stock_button)))


    # Actions

    def clean_adress(self):
        self.clean = self.get_clean_adress()
        self.clean.click()

    def add_adress(self):
        self.get_adress_locator().send_keys('Москва, Сумской проезд, 9Б')

    def press_confirm_adress(self):
        self.get_confirm_adress().click()

    def press_suggest_adress(self):
        self.get_suggest_adress().click()

    def press_clear_button(self):
        self.get_clear_button().click()

    def text_in_allert_out_of_stock(self):
        fun = self.get_allert_no_stocks()
        if fun == 1:
            return 1 
        else:
            return self.get_allert_no_stocks().text
    
    def click_ok_allert_out_of_stock(self):
        self.get_allert_no_stocks_button().click()
        

    



    
    # Actions

    def finish(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()
        