from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys 
sys.path.append("C:\\Users\\Blad2\\git_proj\\studing\\proj_selenium")
from pages.logining_page import loginpage, buy_page
from pages.main_page import mainpage
from pages.cart import cartpage
from pages.user_info import user_info
from pages.payment_page import Payment
from pages.finish_page import finish


def test_link_about():
        g = Service('C:\\Users\\Blad2\\git_proj\\studing\\proj_selenium\\base\\chromedriver.exe')
        driver = webdriver.Chrome(service=g)
        enter = loginpage(driver)
        enter.authorization()

        mp = mainpage(driver)
        mp.select_menu_about()

       



"""Cart"""
# chech_cart = cart(driver)
# cart_goods = chech_cart.collecting_price_and_name('cart_page')
# chech_cart.checkout()
