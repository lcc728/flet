# Flex Radio
# 2024-08-19
# https://www.george.tw/2024/08/20/flet-radio/

import flet as ft

def main(page: ft.Page):
    def radio_change(e):
        showText.value = f"你最愛的文字編輯器是：{e.control.value}"
        page.update()

    radio_group = ft.RadioGroup(
        value="",
        content=ft.Column([
            ft.Radio(value="VS Code", label="VS Code"),
            ft.Radio(value="Sublime Text", label="Sublime Text"),
            ft.Radio(value="Notepad++", label="Notepad++")
        ]),
        on_change=radio_change)
    
    showText = ft.Text("")
    page.add(radio_group, showText)

ft.app(target=main)
