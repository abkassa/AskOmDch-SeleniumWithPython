from selenium import webdriver
import time
import unittest
from Pages.AssertionPage import AssertionPage
from Pages.SignUpPage import SignUpPage


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

        # initialize signup page
        signup = SignUpPage(driver)
        signup.click_account_tab()
        time.sleep(2)

        signup.enter_sign_up_details()
        time.sleep(2)

        signup.click_register_button()
        time.sleep(2)

        # Assertion
        sucsess = AssertionPage(driver)
        sucsess.signup_success()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


