# Flet -Greeting 
# 2024-08-29
# 練習 Text, Button 和 TextField

import flet as ft

def main (page: ft.page):
    page.title =" Flet -Greeting" #定義視窗 title
    page.window.width = 450  #定義視窗的寬度
    page.window.height = 300 #定義視窗的高度

    def on_click(e):
        result_text.value = "Hello " + input_text.value
        page.update()

    input_text = ft.TextField(
        label = "Your name:",
        color = "blue",
        border= "underline"
    )  

    send_button = ft.IconButton(
        icon = ft.icons.SEND_ROUNDED,
        icon_color= "red",
        icon_size= 20,
        tooltip= "Send",
        on_click= on_click
    )

    result_text = ft.Text('' , color= ft.colors.BLUE_300)

    page.add(
        input_text,
        send_button,
        result_text 

    )

ft.app(target=main)
