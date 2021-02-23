from selenium.webdriver.common.by import By


class BasePageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn:nth-child(1)')


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:

    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.content h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')


class BasketPageLocators:

    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
