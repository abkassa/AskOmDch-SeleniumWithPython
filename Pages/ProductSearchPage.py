
class ProductSearchPage():
    def __init__(self, driver):
        self.driver = driver
        self.store_tab = "//div[@class='site-primary-header-wrap ast-builder-grid-row-container site-header-focus-item ast-container']//a[.='Store']"
        self.search_box = "//input[@name='s']"
        self.search_button = "//button[.='Search']"
        self.add_to_cart_button = "//button[@name='add-to-cart']"
        self.view_cart_button = "//div[@class='site-primary-header-wrap ast-builder-grid-row-container site-header-focus-item ast-container']//span[@class='count']"

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






