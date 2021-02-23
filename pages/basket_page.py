from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Product is presented, but should not be'

    def should_be_message_that_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text == \
               'Your basket is empty. Continue shopping', 'Message about empty basket is not presented'
