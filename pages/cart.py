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

class cartpage(Base):


    def __init__(self,driver):

        self.driver = driver

        # Locators
        self.checkout = '//button[@id="checkout"]'

        
    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH ,  self.checkout)))
    



    # Actions

    def click_chechout(self):
        self.get_checkout_button().click()
        print('checkout')



    
    # Actions

    def cart_actions(self):

        self.get_current_url()
        self.click_chechout()
 


class buy_page:
    def __init__(self,driver):
        self.path_product_name = driver.find_elements(By.XPATH, value = "//a//div")
        self.path_product_price = driver.find_elements(By.XPATH, value ="//div[@class='inventory_item_price']")
        self.button_add_to_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")))
        self.elemet_massive = [self.path_product_name, self.path_product_price]
        self.cart_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//a[@class="shopping_cart_link"]')))
        

    def collecting_price_and_name(self, name):
        dct = {}
        data_massive = [[j.text for j in i]  for i in self.elemet_massive]
        for i in range(len(data_massive[0])):
            dct.setdefault(name, {})
            dct[name].update({data_massive[0][i] : data_massive[1][i]})

        return dct

    def add_goods_in_cart_by_page(self, name):
        
        
        self.add_to_cart = driver.find_element(By.XPATH, value = f"//button[@id='add-to-cart-{name.replace(' ','-').lower()}']")
        self.add_to_cart.click()

    def go_to_cart(self):
        self.cart_button.click()




