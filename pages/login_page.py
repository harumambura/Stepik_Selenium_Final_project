from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators, MainPageLocators
import time


class LoginPage(BasePage):

    def register_new_user(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email = str(time.time()) + "@i.ua"
        self.email_input.send_keys(email)
        self.password1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        password = "imapassword789789"
        self.password1.send_keys(password)
        self.password2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        self.password2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_ENTER).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert self.browser.current_url.count('login') != 0, 'No word "login" in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no registration form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "registration form found"
