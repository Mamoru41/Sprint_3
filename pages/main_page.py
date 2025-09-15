from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def open_main_page(self):
        self.open(self.base_url)

    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON_ON_MAIN)

    def click_personal_account_button(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_stellar_burger_logo(self):
        self.click(MainPageLocators.STELLAR_BURGER_LOGO)

    def click_buns_section(self):
        self.click(MainPageLocators.BUNS_SECTION)

    def click_sauces_section(self):
        self.click(MainPageLocators.SAUCES_SECTION)

    def click_fillings_section(self):
        self.click(MainPageLocators.FILLINGS_SECTION)

    def is_section_active(self, section_locator):
        element = self.find_element(section_locator)
        return "tab_tab_type_current" in element.get_attribute("class")

    def is_place_order_button_visible(self):
        return self.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)