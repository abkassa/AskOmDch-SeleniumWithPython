
class SignUpPage():
    def __init__(self, driver):
        self.driver = driver
        self.account_tab = "//div[@class='site-primary-header-wrap ast-builder-grid-row-container site-header-focus-item ast-container']//a[.='Account']"
        self.username = "//input[@id='reg_username']"
        self.email = "//input[@id='reg_email']"
        self.password = "//input[@id='reg_password']"
        self.register_button = "//button[@name='register']"

    def click_account_tab(self):
        self.driver.find_element_by_xpath(self.account_tab).click()

    def enter_sign_up_details(self):
        self.driver.find_element_by_xpath(self.username).clear()
        self.driver.find_element_by_xpath(self.username).send_keys('abk19')
        self.driver.find_element_by_xpath(self.email).clear()
        self.driver.find_element_by_xpath(self.email).send_keys('abk19@gmail.com')
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(self.password).send_keys('Pass@abk')

    def click_register_button(self):
        self.driver.find_element_by_xpath(self.register_button).click()






