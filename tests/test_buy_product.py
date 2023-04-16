from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.chrome.options import Options
sys.path.append("C:\\Users\\Blad2\\git_proj\\studing\\final_proj_sel_vkus")
from pages.main_page import mainpage
from pages.cart import cartpage

from pages.payment_page import Payment
from pages.delivery import finish
from pages.catalog import catalogpage
from base.base_class import Base
from time import sleep




@pytest.mark.run(order = 1)
def test_select_product_1():
        print('Start test 1')
        g = Service('C:\\Users\\Blad2\\git_proj\\studing\\final_proj_sel_vkus\\base\\chromedriver.exe')
        driver = webdriver.Chrome(service=g)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--log-level=3')
        enter = mainpage(driver)

        enter.go_to_catalog()
        catalog_actions = catalogpage(driver)
        catalog_actions.go_to_cooked_food()
        products_to_buy_in_catalog = catalog_actions.create_dict_of_products()
        catalog_actions.close_cookies()
        choosed_product = Base(driver).chosed_product(products_to_buy_in_catalog)
        catalog_actions.add_to_cart_ready_food(choosed_product)

        delivery_info = finish(driver)
        delivery_info.add_adress()
        delivery_info.press_suggest_adress()
        delivery_info.press_confirm_adress()
        delivery_info.press_clear_button()
        
        if isinstance(delivery_info.text_in_allert_out_of_stock(), str):
                delivery_info.click_ok_allert_out_of_stock()
                products_to_buy_in_catalog = catalog_actions.create_dict_of_products()
                choosed_product = Base(driver).chosed_product(products_to_buy_in_catalog)
                catalog_actions.add_to_cart_ready_food(choosed_product)
        catalog_actions.go_to_cart()

        Base(driver).assert_url('https://vkusvill.ru/cart/')

        cart_actions = cartpage(driver)
        cart_actions.post_name_locator("Iliya")
        cart_actions.post_email_locator('blad2796@rambler.ru')
        cart_actions.post_phone_locator('9653245047')
        cart_actions.click_therminal_payment()
        cart_actions.post_flat_locator('1')
        cart_actions.click_submit()
        cart_actions.pass_allert_autorization()


        final_page = Payment(driver)
        final_page.click_button_good()
        final_page.click_button_cancel_order()
        final_page.click_button_cancel_allert()
        final_page.click_button_ok()



       
        

        



        # ui = user_info(driver)
        # ui.add_user_info()
        # pp = Payment(driver)
        # pp.click_button_finish()
        # fp = finish(driver)
        # fp.finish()
        print('Finish test 1')
        # driver.close()



