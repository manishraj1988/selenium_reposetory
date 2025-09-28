from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import config

class HomePage(BasePage):
    # Locators
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".welcome-message")
    LOGOUT_BUTTON = (By.ID, "logout")
    USER_PROFILE = (By.CLASS_NAME, "user-profile")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{config.BASE_URL}/home"

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MESSAGE)

    def is_logged_in(self):
        return self.is_visible(self.USER_PROFILE, timeout=5)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)