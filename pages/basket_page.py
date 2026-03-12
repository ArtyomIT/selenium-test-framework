from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty (but should be for this test)'

    def should_be_empty_basket(self):
        assert 'Ваша корзина пуста' or "Your basket is empty" in self.browser.find_element(*BasketPageLocators.IS_BASKET_EMPTY).text, ('Text about basket empty is disappeared')