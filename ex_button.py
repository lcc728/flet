# Flet button
# 2024-08-14
# https://www.george.tw/2024/08/15/flet-button/

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.TextButton(text="Text button"),
        ft.IconButton(
            icon="favorite",
            icon_color="red",
            icon_size=20,
            tooltip="IconButton ",
        ),
        ft.FilledButton(text="Filled button"),        
        ft.FilledTonalButton("FilledTonalButton with icon", icon="favorite", icon_color= "red"),  
        ft.OutlinedButton(text="Outlined button" , icon="favorite"),
        ft.ElevatedButton(text="Elevated button",url="https://www.george.tw", url_target ="BLANK"),
        ft.FloatingActionButton(icon="favorite",bgcolor="red"),

        
    )
ft.app(target=main)
