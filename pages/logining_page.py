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

class loginpage(Base):


    def __init__(self,driver):
        super().__init__(driver)
        self.base_url = 'https://www.saucedemo.com/'
        self.driver = driver

        # Locators
        self.user_name = '//*[@id="user-name"]'
        self.user_password = '//*[@id="password"]'
        self.check_in = '//input[@id="login-button"]'
        self.check_word = '//span[@class="title"]'

        
    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="user-name"]')))
    
    def get_password(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.user_password)))

    def get_login_button(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.check_in)))
    
    def get_check_word(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.check_word)))


    # Actions

    def input_user_name(self, name):
        self.get_user_name().send_keys(name)
        print('input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input user password')

    def click_button_login(self):
        self.get_login_button().click()
        print('click login')
    
    # Actions

    def authorization(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password('secret_sauce')
        self.click_button_login()
        self.assert_word(self.get_check_word(), "Products")

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




