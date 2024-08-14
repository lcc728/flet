# Flet - TextField
# 2024-08-14
# https://www.george.tw/2024/08/15/flet-textfield/
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.TextField(
            label="帳號:", 
            hint_text="你的帳號", 
            icon=ft.icons.PERSON, 
            color="blue", 
            border = "outline", 
            border_color="green",
            bgcolor="amber",
            text_size= 30,
            text_align="center",
            border_radius= ft.border_radius.all(10),
            border_width= 5,
            cursor_color= "red",
            focused_bgcolor="green",
            focused_border_color="amber", 
            keyboard_type = ft.KeyboardType.NUMBER,
            ),
        ft.TextField(
            label="密碼:",
            password=True,
            can_reveal_password=True,
            hint_text="請輸入密碼",
            helper_text="忘記密碼請聯絡管理員",
            color="red",
            icon=ft.icons.KEY,
            max_length=15,

        ),
        ft.TextField(
            label="備註:",
            multiline=True,
            min_lines=5,
            max_lines=10,
            icon=ft.icons.NOTE,
            border=ft.InputBorder.UNDERLINE
        ),    
    )
ft.app(target=main)
