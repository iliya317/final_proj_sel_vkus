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

class catalogpage(Base):


    def __init__(self,driver):
        super().__init__(driver)

        # Locators
        self.ready_food = '//img[@alt="Готовая еда"]'
        self.product_cards = '//a[@class="ProductCard__link rtext _desktop-md _mobile-sm gray900 js-datalayer-catalog-list-name"]'
        self.cart_button = "//a[@onclick=\"analyticsGoal('ShopHeaderBasketClick');\"]" #'//div[@class="HeaderBuy__Col _cart"]' #"//a[@class = 'HeaderCart HeaderElem js-delivery__basketHeader ']" #"//span[@class='HeaderCart__ImgWrp']" #
        self.delivery_info_button = "//span[@class ='HeaderBuy__SelectTitleInner _action']" #"//span[@class ='HeaderBuy__SelectType _action js-delivery__shopselect--form-show _no_delivery']"#"//div[@class='HeaderBuy__Select']" #"//span[@class ='HeaderBuy__SelectType _action js-delivery__shopselect--form-show _no_delivery']"
        self.close_cookie = '//button[@class = "Cookie__close js-cookie-warning-close"]'
 

        
    # Getters
    def card_button(self, id):
        self.add_to_cart_locator = f'//button[@data-product-id="{id}"]'
        return self.add_to_cart_locator

    def cooked_food_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.ready_food)))
    
    def cooked_food(self,id):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.card_button(id))))
        
    def get_cart_button(self):
        
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.cart_button)))
    
    def get_delivery_info_button(self):
        WebDriverWait(self.driver, 30).until(EC.staleness_of(self.delivery_info_button))
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH , self.delivery_info_button)))

    def get_close_cookie(self):
        #WebDriverWait(self.driver, 30).until(EC.staleness_of(self.delivery_info_button))
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.close_cookie)))

    # Actions

    def create_dict_of_products(self):
        dct = {}
        self.driver.implicitly_wait(5)
        card_elements = self.driver.find_elements(By.XPATH, self.product_cards)
        for i in card_elements:
            dct[int(i.get_attribute('href').split('-')[-1][:-5])] = i.get_attribute('title')
        return dct
        


    def add_to_cart_ready_food(self,id):
        self.cooked_food(id).click()

    def go_to_cooked_food(self):
        self.driver.execute_script("arguments[0].click();", self.cooked_food_category())

    def go_to_cart(self):
        self.driver.execute_script("arguments[0].click();", self.get_cart_button())

    
    def go_to_delivery_info(self):
        self.get_delivery_info_button().click()

    def close_cookies(self):
        self.get_close_cookie().click()



