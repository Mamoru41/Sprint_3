from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators


class ProfilePage(BasePage):
    def open_profile_page(self):
        self.open(f"{self.base_url}/account/profile")

    def get_name_value(self):
        return self.find_element(ProfilePageLocators.NAME_INPUT).get_attribute("value")

    def get_email_value(self):
        return self.find_element(ProfilePageLocators.EMAIL_INPUT).get_attribute("value")

    def click_logout_button(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    def click_constructor_button(self):
        # Находим кнопку конструктора через главную страницу
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_stellar_burger_logo(self):
        self.click(MainPageLocators.STELLAR_BURGER_LOGO)

    def is_profile_page_displayed(self):
        return self.is_element_present(ProfilePageLocators.PROFILE_HEADER)

    def is_logout_successful(self):
        return self.is_element_present(LoginPageLocators.LOGIN_HEADER)