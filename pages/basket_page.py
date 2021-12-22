from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
from .product_page import ProductPage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), 'Basket is no empty, but should be'

    def basket_is_empty_message(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        assert message.count('empty') != 0
