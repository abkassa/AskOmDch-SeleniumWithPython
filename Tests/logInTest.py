from selenium import webdriver
import time
import unittest

from Pages.AssertionPage import AssertionPage
from Pages.LogInPage import LogInPage


class AskOmDchLogin(unittest.TestCase):

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

        # initialize login page
        login = LogInPage(driver)
        login.click_account_tab()
        time.sleep(4)

        login.enter_login_details()
        time.sleep(4)

        login.click_login_button()
        time.sleep(4)

        # Assertion
        sucsess = AssertionPage(driver)
        sucsess.login_success()



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


