# Flet - Oxford 3000,  常用 3000 字字卡
# 2024-09-23
# https://www.george.tw/2024/09/24/flet-oxford3000/
# CSV Files: https://github.com/lcc728/Oxford_3000

import flet as ft
import pandas as pd
import random

def main(page: ft.Page):
    page.title = "單字卡"
    page.window.width = 502
    page.window.height = 482

    current_index = 0
    is_front = True
    df = pd.DataFrame()

    alphabet_options = [ft.dropdown.Option(chr(i)) for i in range(ord('A'), ord('Z') + 1)]

    def load_csv(letter):
        nonlocal df, current_index, is_front
        file_name = f"letter_{letter.lower()}.csv"
        df = pd.read_csv(file_name)
        current_index = random.randint(0, len(df) - 1)
        is_front = True
        card.content = get_card_content(current_index, front=True)
        page.update()

    def get_card_content(index, front=True):
        if front:
            return ft.Column([
                ft.Text(df.loc[index, 'Word'], size=32),
                ft.Text(df.loc[index, '詞性'], size=18),
                ft.Row([
                    ft.Text("EN:", size=20),
                    ft.Text(df.loc[index, 'EN'], size=20, color=ft.colors.RED_500),
                    ft.Text("US:", size=20),
                    ft.Text(df.loc[index, 'US'], size=20, color=ft.colors.RED_500),
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ), 


            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        else:
            return ft.Column([
                ft.Text(df.loc[index, '中文'], size=20),
                ft.Text("例句:  " + df.loc[index, '例句'], size=20),
                ft.Text('中文說明:  ' + df.loc[index, '中文說明'], size=20)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)


    def update_card():
        nonlocal current_index, is_front
        while True:
            new_index = random.randint(0, len(df) - 1)
            if new_index != current_index:
                break
        current_index = new_index
        is_front = True
        card.content = get_card_content(current_index, front=True)
        page.update()

    def toggle_card():
        nonlocal is_front
        is_front = not is_front
        card.content = get_card_content(current_index, front=is_front)
        page.update()

    def on_dropdown_change(e):
        load_csv(e.control.value)

    card = ft.Container(
        content=ft.Text("請選擇字母", size=32),
        alignment=ft.alignment.center,
        width=500,
        height=300,
        bgcolor=ft.colors.BLUE_50,
        border_radius=10,
        on_click=lambda e: toggle_card()
    )
  
    dropdown = ft.Dropdown(
        options=alphabet_options,
        value="A",
        on_change=on_dropdown_change
    )
    
    page.add(
        ft.Column([
            dropdown,
            card,
            ft.Row([
                ft.ElevatedButton("下一題", on_click=lambda e: update_card()),
                ft.Text("點一下字卡看中文說明及例句 ")
            ],
            
            ),
          
        ])
    )
    load_csv("A")

ft.app(target=main)
