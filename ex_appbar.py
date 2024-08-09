# AppBar
# 2024-08-09
#
import flet as ft

def main(page: ft.Page):

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TAG_FACES),
        leading_width=40,
        title=ft.Text("My APP"),
        center_title=False,
        bgcolor=ft.colors.LIGHT_BLUE_ACCENT_200,
        actions=[
            ft.IconButton(ft.icons.CAKE),
            ft.IconButton(ft.icons.COOKIE),
            ft.IconButton(ft.icons.BAKERY_DINING_OUTLINED),
       ],     
    )

    page.add(ft.Text("Hello World"))

ft.app(target=main)
