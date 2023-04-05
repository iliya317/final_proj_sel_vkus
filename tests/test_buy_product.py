from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
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


@pytest.mark.run(order = 2)
def test_select_product_1():
        print('Start test 1')
        g = Service('C:\\Users\\Blad2\\git_proj\\studing\\proj_selenium\\base\\chromedriver.exe')
        driver = webdriver.Chrome(service=g)
        enter = loginpage(driver)
        enter.authorization()

        mp = mainpage(driver)
        mp.select_product_1()

        cp = cartpage(driver)
        cp.cart_actions()

        # ui = user_info(driver)
        # ui.add_user_info()
        # pp = Payment(driver)
        # pp.click_button_finish()
        # fp = finish(driver)
        # fp.finish()
        print('Finish test 1')
        driver.close()



@pytest.mark.run(order = 1)
def test_select_product_2():
        print('Start test 2')
        g = Service('C:\\Users\\Blad2\\git_proj\\studing\\proj_selenium\\base\\chromedriver.exe')
        driver = webdriver.Chrome(service=g)
        enter = loginpage(driver)
        enter.authorization()

        mp = mainpage(driver)
        mp.select_product_2()

        cp = cartpage(driver)
        cp.cart_actions()

        # ui = user_info(driver)
        # ui.add_user_info()
        # pp = Payment(driver)
        # pp.click_button_finish()
        # fp = finish(driver)
        # fp.finish()
        print('Finish test 2')
        driver.close()

@pytest.mark.run(order = 3)
def test_select_product_3():
        print('Start test 3')
        g = Service('C:\\Users\\Blad2\\git_proj\\studing\\proj_selenium\\base\\chromedriver.exe')
        driver = webdriver.Chrome(service=g)
        enter = loginpage(driver)
        enter.authorization()

        mp = mainpage(driver)
        mp.select_product_3()

        cp = cartpage(driver)
        cp.cart_actions()

        # ui = user_info(driver)
        # ui.add_user_info()
        # pp = Payment(driver)
        # pp.click_button_finish()
        # fp = finish(driver)
        # fp.finish()
        print('Finish test 3')
        driver.close()
        


