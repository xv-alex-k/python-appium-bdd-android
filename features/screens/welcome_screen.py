from appium.webdriver.common.mobileby import MobileBy

from .base_screen import BaseScreen


class Welcome(BaseScreen):
    BUTTON_CREATE_NEW_ACCOUNT = (MobileBy.ID, "sign_up_with_email_or_phone")
    BUTTON_LOGIN = (MobileBy.ID, "log_in_button")

    def _verify_screen(self):
        self.on_this_screen(self.BUTTON_CREATE_NEW_ACCOUNT, self.BUTTON_LOGIN)

    def tap_login(self):
        self.tap(self.BUTTON_LOGIN)
