from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_login_page(self):
        self.click_add_to_basket_button()

    def click_add_to_basket_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_successful_addition(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), "Item was not added to order"

    def should_have_same_name(self):
        basket_string = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        basket_text = basket_string.text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_text = product_name.text
        assert product_text in basket_text, "was added another product"


    def should_have_same_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        basket_price_text = basket_price.text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        assert product_price_text in basket_price_text, "price differ"


#
