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

        super().__init__(driver)
        self.base_url = 'https://vkusvill.ru/'
        self.driver.get(self.base_url)
        self.driver.maximize_window()


        # Locators
        self.button_catalog = '//a[@id="js-header-catalog-shower"]' #//div[@class="HeaderLevelProdsSet__Col _goods-link swiper-slide swiper-slide-active"]'


        
    # Getters

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , self.button_catalog)))


    # Actions

    def go_to_catalog(self):
        self.get_button_catalog().click()
        print('went to catalog')


    
    # Actions

    
        
        


