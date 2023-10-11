import flet

from flet import *


def main(page: flet.Page) -> None:
    page.title = "Login"
    page.vertical_aligment = flet.MainAxisAlignment.CENTER
    page.theme_mode = flet.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400

if __name__ == "__main__":
    flet.app(target=main)