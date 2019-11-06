from appium import webdriver


def before_all(context):
    desired_caps = {"platformName": "Android",
                    "deviceName": "Android Emulator",
                    "appPackage": "com.instagram.android",
                    "appActivity": "com.instagram.mainactivity.LauncherActivity",
                    "automationName": "UiAutomator2"}
    executor_url = "http://localhost:4723/wd/hub"
    context.driver = webdriver.Remote(executor_url, desired_caps)


def before_scenario(context, scenario):
    context.driver.reset()


def after_all(context):
    context.driver.quit()
