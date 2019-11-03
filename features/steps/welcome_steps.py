import time

from behave import step

from features import screens


@step("I login to instagram")
def login(context):
    login = "pyautomation"
    password = "Ab1234567890!"
    welcome_screen = screens.Welcome(context.driver)
    welcome_screen.tap_login()
    login_screen = screens.Login(context.driver)
    login_screen.type_login(login)
    login_screen.type_password(password)
    login_screen.tap_login()
    time.sleep(10)
