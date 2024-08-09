# AppBar
# 2024-08-09
# https://www.george.tw/2024/08/10/flet-appbar/
import flet as ft

    def main(page: ft.Page):
        page.appbar = ft.AppBar(                        #產生一個 AppBar
            leading=ft.Icon(ft.icons.TAG_FACES),        #在 leading 的位置放了一個 icon
            leading_width=40,                           #指定寬度為 40
            title=ft.Text("My APP"),                    # Title為 文字: MyAPP
            center_title=False,                         #關閉文字的置中對齊  
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_200,    #背景色設定為  LIGHT_BLUE_ACCENT_200
            actions=[                                   #在 action 的位置放三個 icon
               ft.IconButton(ft.icons.CAKE),
               ft.IconButton(ft.icons.COOKIE),
               ft.IconButton(ft.icons.BAKERY_DINING_OUTLINED),
           ],     
        )
        page.add(ft.Text("Hello World"))
ft.app(target=main)

#  Flutter AppBar https://api.flutter.dev/flutter/material/AppBar-class.html
#  Flet AppBar  https://flet.dev/docs/controls/appbar/
