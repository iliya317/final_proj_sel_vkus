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

class user_info(Base):


    def __init__(self,driver):

        self.driver = driver

        # Locators
        self.first_name ='//input[@placeholder="First Name"]'
        self.last_name = '//input[@placeholder="Last Name"]'
        self.zip_elem = '//input[@placeholder="Zip/Postal Code"]'
        self.button_continue = '//input[@id="continue"]'   

        
    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.first_name)))
    
    def get_last_name(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.last_name)))
    
    def get_zip_elem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.zip_elem)))
    
    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.button_continue)))



    # Actions

    def add_first_name(self, name):
        self.get_first_name().send_keys(name)
        print('name added')

    def add_last_name(self, sec_name):
        self.get_last_name().send_keys(sec_name)
        print('sec name added')
    
    def add_zip_elem(self, zip):
        self.get_zip_elem().send_keys(zip)
        print('zip added')

    def click_button_continue(self):
        self.get_button_continue().click()
        print('continue pressed')


    
    # Actions

    def add_user_info(self):

        self.add_first_name('iliya')
        self.add_last_name('iliya')
        self.add_zip_elem('iliya')
        self.click_button_continue()
        


# class buy_page:
#     def __init__(self,driver):
#         self.path_product_name = driver.find_elements(By.XPATH, value = "//a//div")
#         self.path_product_price = driver.find_elements(By.XPATH, value ="//div[@class='inventory_item_price']")
#         self.button_add_to_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")))
#         self.elemet_massive = [self.path_product_name, self.path_product_price]
#         self.cart_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//a[@class="shopping_cart_link"]')))
        

#     def collecting_price_and_name(self, name):
#         dct = {}
#         data_massive = [[j.text for j in i]  for i in self.elemet_massive]
#         for i in range(len(data_massive[0])):
#             dct.setdefault(name, {})
#             dct[name].update({data_massive[0][i] : data_massive[1][i]})

#         return dct

#     def add_goods_in_cart_by_page(self, name):
        
        
#         self.add_to_cart = driver.find_element(By.XPATH, value = f"//button[@id='add-to-cart-{name.replace(' ','-').lower()}']")
#         self.add_to_cart.click()

#     def go_to_cart(self):
#         self.cart_button.click()




