from selenium.webdriver.common.by import By


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    CART_LINK = (By.XPATH, '//a[contains(text(), "basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_ENTER = (By.CSS_SELECTOR, '[name="login_submit"]')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_ENTER = (By.CSS_SELECTOR, '[value="Register"]')

class ProductPageLocators():

    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    ADD_TO_CART = (By.CSS_SELECTOR, '#add_to_basket_form')
    PRODUCT_ADDED_IN_CART = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-success  fade in"] strong')
    PRICE_PRODUCT_ADDED_IN_CART = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"] strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"]')

class BasketPageLocators():

    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '[class="basket-title hidden-xs"]')
    BASKET_STATUS = (By.XPATH, '//p[contains(text(), "Your basket")]')
