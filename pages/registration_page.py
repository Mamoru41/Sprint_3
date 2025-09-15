from .base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def open_registration_page(self):
        self.open(f"{self.base_url}/register")

    def set_name(self, name):
        self.set_text(RegistrationPageLocators.NAME_INPUT, name)

    def set_email(self, email):
        self.set_text(RegistrationPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        self.set_text(RegistrationPageLocators.PASSWORD_INPUT, password)

    def click_register_button(self):
        self.click(RegistrationPageLocators.REGISTER_BUTTON)

    def click_login_link(self):
        self.click(RegistrationPageLocators.LOGIN_LINK)

    def register_user(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_register_button()

    def is_registration_page_displayed(self):
        return self.is_element_present(RegistrationPageLocators.REGISTRATION_HEADER)

    def is_password_error_displayed(self):
        return self.is_element_present(RegistrationPageLocators.PASSWORD_ERROR)