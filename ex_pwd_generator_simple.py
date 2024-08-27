# Flet Password generator (Simple version)
# 2024-08-19 
# https://www.george.tw/2024/08/19/flet-password-generator-simple-version/

import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "密碼產生器"
    chars = string.ascii_letters + string.digits + string.punctuation

    
    def generate_password(e):
        length = int(slider.value)
        pwd = ''.join(random.sample(chars,length))
        password.value = pwd
        page.update()

    slider = ft.Slider(min=6, max=30, divisions=24, label="{value}位", value=12)
    password = ft.Text(value="", style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    generate_button = ft.ElevatedButton("產生密碼", on_click=generate_password)

    page.add(
        ft.Text("選擇密碼的長度:"),
        slider,
        generate_button,
        ft.Text("你要的密码是:"),
        password
    )

ft.app(target=main)
