from .base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def open_forgot_password_page(self):
        self.open(f"{self.base_url}/forgot-password")

    def set_email(self, email):
        self.set_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)

    def click_login_link(self):
        self.click(ForgotPasswordPageLocators.LOGIN_LINK)

    def is_forgot_password_page_displayed(self):
        return self.is_element_present(ForgotPasswordPageLocators.FORGOT_PASSWORD_HEADER)