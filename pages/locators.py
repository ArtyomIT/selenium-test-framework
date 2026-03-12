from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CHECK_BASKET = (By.XPATH, '//a[contains(@href, "basket")]')

    USER_ICON = (By.XPATH, "//i[@class = 'icon-user']")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_EMAIL = (By.XPATH, "//input[@id ='id_registration-email']")
    REGISTER_PASSWORD_1 = (By.XPATH, "//input[@id ='id_registration-password1']")
    REGISTER_PASSWORD_2 = (By.XPATH, "//input[@id ='id_registration-password2']")

    BUTTON_SUBMIT_REGISTRATION = (By.XPATH, "//button[@name = 'registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form button')

    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_ITEM_PRICE = (By.XPATH, "//div[contains(@class,'basket-mini')]")

    BOOK_NAME_ON_PAGE = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    BOOK_NAME_IN_TEXT_MESSAGE = (By.XPATH, "//div[@class = 'alertinner ']//strong")

class BasketPageLocators():
    IS_BASKET_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
