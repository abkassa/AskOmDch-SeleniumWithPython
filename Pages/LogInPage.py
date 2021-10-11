
class LogInPage():
    def __init__(self, driver):
        self.driver = driver
        self.account_tab = "//div[@class='site-primary-header-wrap ast-builder-grid-row-container site-header-focus-item ast-container']//a[.='Account']"
        self.username = "//input[@id='username']"
        self.password = "//input[@id='password']"
        self.login_button = "//button[@name='login']"

    def click_account_tab(self):
        self.driver.find_element_by_xpath(self.account_tab).click()

    def enter_login_details(self):
        self.driver.find_element_by_xpath(self.username).clear()
        self.driver.find_element_by_xpath(self.username).send_keys('abk1')
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(self.password).send_keys('Pass@abk')

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()



