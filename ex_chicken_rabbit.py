# Flet - Chicken and Rabbit in a Cage 雞免同籠
# 2024-08-27
# https://www.george.tw/2024/08/27/flet-chicken-and-rabbit-in-a-cage/

import flet as ft

def main(page: ft.Page):
    page.title = "雞兔同籠"
    def calculate(e):
        try:
            H = int(H_input.value)
            F = int(F_input.value)
           
            C=  int((4 * H - F )/2)
            R = H - C
           

            result.value = f"雞有 {C} 隻，兔子有 {R} 隻"
        except ValueError:
            result.value = "請輸入數字"

        page.update()

    H_input = ft.TextField(label="雞兔同籠共幾隻", icon=ft.icons.CRUELTY_FREE)
    F_input = ft.TextField(label="一共有幾隻腳",  icon=ft.icons.QUESTION_MARK)
    calculate_button = ft.ElevatedButton(text="計算", on_click=calculate)
    result = ft.Text()

    page.add(
        
            H_input,
            F_input,
            calculate_button,
            result
        
    )

ft.app(target=main)
