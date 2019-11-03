from appium.webdriver.common.mobileby import MobileBy

from .base_screen import BaseScreen


class Login(BaseScreen):

    TEXT_LOGIN = (MobileBy.ID, "login_username")
    TEXT_PASSWORD = (MobileBy.ID, "password")
    BUTTON_LOGIN = (MobileBy.ID, "next_button")

    def _verify_screen(self):
        self.on_this_screen(self.TEXT_LOGIN, self.TEXT_PASSWORD)

    def type_login(self, login):
        self.enter_text(self.TEXT_LOGIN, login)

    def type_password(self, password):
        self.enter_text(self.TEXT_PASSWORD, password)

    def tap_login(self):
        self.tap(self.BUTTON_LOGIN)
