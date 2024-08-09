# Flet - Hello World
# 2024-08-09 
# https://www.george.tw/2024/08/10/flet-hello-world/

import flet as ft                           #import Flet 模組

def main(page: ft.Page):                    #定義 Main，內有一個參數 page 用來定義各種 Flet 的元件   

    page.add(ft.Text("Hello World!"))       #增加一個 flet 的 text widget, 裡面放 Hello world 的文字

ft.app(target=main)                         # 指定 flet 的入口為 main 
