from pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_add_to_basket_button()
        time.sleep(2)
        product_page.should_be_successful_addition()
        product_page.should_have_same_name()
        #product_page.should_have_same_price()

        #login_page = LoginPage(browser, browser.current_url)
        #login_page.should_be_login_page()