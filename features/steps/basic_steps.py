from behave import step

from features import screens


@step("I am on {screen_name} screen")
def verify_screen(context, screen_name):
    screen_class = screens.factory(screen_name)
    screen_class(context.driver)
