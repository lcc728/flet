# Flet Icon
# 2024-08-13
# https://www.george.tw/2024/08/14/flet-icon/
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Icon(name=ft.icons.FAVORITE, color="red", size=50),
        ft.Icon(name=ft.icons.FAVORITE, color="red", size=50, opacity=0.2),
        ft.Icon(name=ft.icons.FAVORITE, color="red", size=50, semantics_label="Heart"),
        ft.Icon(name=ft.icons.FAVORITE, color="red", size=50, tooltip="Heart"),
        ft.Icon(name=ft.icons.FAVORITE, color="red", size=50, rotate=45),
    )
ft.app(target=main)
