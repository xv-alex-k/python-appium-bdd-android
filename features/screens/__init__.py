from .base_screen import BaseScreen
from .login_screen import Login
from .welcome_screen import Welcome

screen_map = {"Login": Login,
              "Welcome": Welcome}


def factory(screen_name: str):
    return screen_map[screen_name]
