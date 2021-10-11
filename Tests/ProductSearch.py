from selenium import webdriver
import time
import unittest

from Pages.AssertionPage import AssertionPage
from Pages.ProductSearchPage import ProductSearchPage


class AskOmDchSignUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # initialize web driver
        cls.driver = webdriver.Chrome("E:/Projects/python/test/resources/drivers/windows/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01(self):
        # Open URL
        driver = self.driver
        driver.get('https://askomdch.com/')

        # initialize Product Search page
        product_search = ProductSearchPage(driver)
        product_search.click_store_tab()
        time.sleep(2)

        product_search.enter_search_item()
        time.sleep(2)

        product_search.click_search_button()
        time.sleep(2)

        product_search.click_add_to_cart_button()
        time.sleep(2)

        product_search.click_view_cart_button()
        time.sleep(2)

        # Assertion
        success = AssertionPage(driver)
        success.search_success()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


