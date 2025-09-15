from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def open_login_page(self):
        self.open(f"{self.base_url}/login")

    def set_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def click_register_link(self):
        self.click(LoginPageLocators.REGISTER_LINK)

    def click_forgot_password_link(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def is_login_page_displayed(self):
        return self.is_element_present(LoginPageLocators.LOGIN_HEADER)