class AssertionPage():
    # Order Success
    def __init__(self, driver):
        self.driver = driver
        self.order_success_message = "//p[@class='woocommerce-notice woocommerce-notice--success woocommerce-thankyou-order-received']"
        self.login_success_message = "//h1[@class='has-text-align-center']"
        self.signup_success_message = "//h1[@class='has-text-align-center']"
        self.search_success_message = "//h1[@class='has-text-align-center']"

    def order_success(self):
        msg = self.driver.find_element_by_xpath(self.order_success_message).text
        print(msg)

    # Login Success
    def login_success(self):
        msg = self.driver.find_element_by_xpath(self.login_success_message).text
        print(msg)

    # Signup Success
    def signup_success(self):
        msg = self.driver.find_element_by_xpath(self.signup_success_message).text
        print(msg)

    # Product Search Success
    def search_success(self):
        msg = self.driver.find_element_by_xpath(self.search_success_message).text
        print(msg)

