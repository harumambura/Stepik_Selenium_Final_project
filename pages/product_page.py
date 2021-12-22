from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def get_added_product_name(self):
        product_added_in_cart_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_added_in_cart_name

    def get_added_product_price(self):
        product_added_in_cart_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_added_in_cart_price

    def add_to_cart(self):
        product_added_in_cart_name = self.get_added_product_name()
        product_added_in_cart_price = self.get_added_product_price()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        products_in_cart_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_ADDED_IN_CART)
        product_in_cart_name = products_in_cart_name[0].text
        products_in_cart_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_CART).text
        assert product_in_cart_name == product_added_in_cart_name, 'Item name in basket does not match added item name'
        assert products_in_cart_price == product_added_in_cart_price, 'Item price in basket does not match added item price'

    def add_promo_to_cart(self, browser, link):
        product_added_in_cart_name = self.get_added_product_name()
        product_added_in_cart_price = self.get_added_product_price()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        bp = BasePage(browser, link)
        bp.solve_quiz_and_get_code()
        products_in_cart_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_ADDED_IN_CART)
        product_in_cart_name = products_in_cart_name[0].text
        products_in_cart_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_CART).text
        assert product_in_cart_name == product_added_in_cart_name, 'Item name in basket does not match added item name'
        assert products_in_cart_price == product_added_in_cart_price, 'Item price in basket does not match added item price'

    def should_not_be_success_message_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'There is success message, but should not be'

    def should_not_be_success_message_element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'There is success message, but should not be'
