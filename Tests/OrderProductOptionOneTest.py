from selenium import webdriver
import time
import unittest
from Pages.AssertionPage import AssertionPage
from Pages.OrderProductOptionOnePage import OrderProductOptionOnePage
from Pages.LogInPage import LogInPage


class AskOmDchOrderOptionOne(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # initialize web driver
        cls.driver = webdriver.Chrome("E:/Projects/python/test/resources/drivers/windows/chromedriver.exe")
        cls.driver.maximize_window()

    def test_01(self):
        # Open URL
        driver = self.driver
        driver.get('https://askomdch.com/')

        # initialize Order page
        order_option_one = OrderProductOptionOnePage(driver)
        order_option_one.click_store_tab()
        time.sleep(2)

        order_option_one.enter_search_item()
        time.sleep(2)

        order_option_one.click_search_button()
        time.sleep(2)

        order_option_one.click_add_to_cart_button()
        time.sleep(2)

        order_option_one.click_view_cart_button()
        time.sleep(2)

        order_option_one.click_proceed_to_checkout_button()
        time.sleep(2)

        order_option_one.click_click_here_to_login_button()
        time.sleep(2)

        # Initialize login page to proceed
        login_to_proceed = LogInPage(driver)
        login_to_proceed.enter_login_details()
        time.sleep(2)

        login_to_proceed.click_login_button()
        time.sleep(2)

        finalize_order = OrderProductOptionOnePage(driver)
        finalize_order.enter_billing_details()
        time.sleep(4)

        finalize_order.click_place_order_button()
        time.sleep(2)

        # Assertion
        sucsess = AssertionPage(driver)
        sucsess.order_success()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


