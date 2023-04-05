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

class mainpage(Base):


    def __init__(self,driver):

        self.driver = driver

        # Locators
        self.product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
        self.product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
        self.product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        self.cart = '//div[@id="shopping_cart_container"]'
        self.check_in = '//input[@id="login-button"]'
        self.check_word = '//span[@class="title"]'
        self.extra_menu = '//button[@id="react-burger-menu-btn"]'
        self.extra_menu_about = '//a[@id="about_sidebar_link"]'

        
    # Getters

    def get_product1_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.product_1)))
    
    def get_product2_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.product_2)))
    
    def get_product3_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.product_3)))
    
    def get_cart(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.cart)))
    
    def get_extra_menu(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.extra_menu)))

    def get_extra_menu_about(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.extra_menu_about)))



    # Actions

    def add_product1_to_cart(self):
        self.get_product1_button().click()
        print('added the product 1')

    def add_product2_to_cart(self):
        self.get_product2_button().click()
        print('added the product 2')

    def add_product3_to_cart(self):
        self.get_product3_button().click()
        print('added the product 3')

    def click_cart(self):
        self.get_cart().click()
        print('Go to the cart')
    
    def click_extra_menu(self):
        self.get_extra_menu().click()

    def click_extra_menu_about(self):
        self.get_extra_menu_about().click()
        


    
    # Actions

    def select_product_1(self):

        self.get_current_url()
        self.add_product1_to_cart()
        self.click_cart()


    def select_product_2(self):

        self.get_current_url()
        self.add_product2_to_cart()
        self.click_cart()


    def select_product_3(self):

        self.get_current_url()
        self.add_product3_to_cart()
        self.click_cart()

    def select_menu_about(self):

        self.get_current_url()
        self.click_extra_menu()
        self.click_extra_menu_about()
        self.assert_url('https://saucelabs.com/')
        
        


