
class OrderProductOptionOnePage():
    def __init__(self, driver):
        self.driver = driver
        self.store_tab = "//div[@class='site-primary-header-wrap ast-builder-grid-row-container site-header-focus-item ast-container']//a[.='Store']"
        self.search_box = "//input[@name='s']"
        self.search_button = "//button[.='Search']"
        self.add_to_cart_button = "//button[@name='add-to-cart']"
        self.view_cart_button = "//div[@class='site-primary-header-wrap ast-builder-grid-row-container site-header-focus-item ast-container']//span[@class='count']"
        self.proceed_to_checkout_button = "//a[contains(.,'Proceed to checkout')]"
        self.click_here_to_login_button = "//a[.='Click here to login']"

        # Belling Details
        self.first_name = "//input[@id='billing_first_name']"
        self.last_name = "//input[@id='billing_last_name']"
        self.company = "//input[@id='billing_company']"
        self.city = "//input[@id='billing_city']"
        self.state = "//input[@id='billing_state']"
        self.zip_code = "//input[@id='billing_postcode']"
        self.email = "//input[@id='billing_email']"
        self.note = "//textarea[@id='order_comments']"

        # place order button
        self.place_order_button = "//button[@id='place_order']"

    def click_store_tab(self):
        self.driver.find_element_by_xpath(self.store_tab).click()

    def enter_search_item(self):
        self.driver.find_element_by_xpath(self.search_box).clear()
        self.driver.find_element_by_xpath(self.search_box).send_keys('Blue Shoes')

    def click_search_button(self):
        self.driver.find_element_by_xpath(self.search_button).click()

    def click_add_to_cart_button(self):
        self.driver.find_element_by_xpath(self.add_to_cart_button).click()

    def click_view_cart_button(self):
        self.driver.find_element_by_xpath(self.view_cart_button).click()

    def click_proceed_to_checkout_button(self):
        self.driver.find_element_by_xpath(self.proceed_to_checkout_button).click()

    def click_click_here_to_login_button(self):
        self.driver.find_element_by_xpath(self.click_here_to_login_button).click()

    def enter_billing_details(self):
        self.driver.find_element_by_xpath(self.first_name).clear()
        self.driver.find_element_by_xpath(self.first_name).send_keys('Abk')
        self.driver.find_element_by_xpath(self.last_name).clear()
        self.driver.find_element_by_xpath(self.last_name).send_keys('Bka')
        self.driver.find_element_by_xpath(self.company).clear()
        self.driver.find_element_by_xpath(self.company).send_keys('AbkCompany')
        self.driver.find_element_by_xpath(self.city).clear()
        self.driver.find_element_by_xpath(self.city).send_keys('MyCity')
        self.driver.find_element_by_xpath(self.state).clear()
        self.driver.find_element_by_xpath(self.state).send_keys('MyState')
        self.driver.find_element_by_xpath(self.zip_code).clear()
        self.driver.find_element_by_xpath(self.zip_code).send_keys('1000')
        self.driver.find_element_by_xpath(self.email).clear()
        self.driver.find_element_by_xpath(self.email).send_keys('ab@gmail.com')
        self.driver.find_element_by_xpath(self.note).clear()
        self.driver.find_element_by_xpath(self.note).send_keys('This is sample order note')

    def click_place_order_button(self):
        self.driver.find_element_by_xpath(self.place_order_button).click()






