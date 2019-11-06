from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver
        self._verify_screen()

    def _verify_screen(self):
        pass

    def get_element(self, locator, timeout=5):
        expected_condition = ec.presence_of_element_located(locator)
        error_message = "Unable to locate element {} in {} seconds".format(locator, timeout)
        return WebDriverWait(self.driver, timeout).until(expected_condition,
                                                         message=error_message)

    def on_this_screen(self, *args, timeout=5):
        for locator in args:
            self.get_element(locator, timeout)

    def tap(self, locator, timeout=5):
        self.get_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=5):
        self.get_element(locator, timeout).send_keys(text)
