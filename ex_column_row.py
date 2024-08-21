# Flet - Column and Row
# 2024-08-21
# https://www.george.tw/2024/08/22/flet-column-row/

import flet as ft

def main(page: ft.Page):
    page.title = "Flet - Column and Row"

    def create_container(text, color):
        return ft.Container(
            content=ft.Text(text, color="white" if color.endswith("500") or color.endswith("900") else "black"),
            bgcolor=color,
            width=50,
            height=50,
            alignment=ft.alignment.center,
        )

    colors = [
        [ft.colors.RED_50, ft.colors.RED_500, ft.colors.RED_900],
        [ft.colors.GREEN_900, ft.colors.GREEN_500, ft.colors.GREEN_50],
        [ft.colors.BLUE_50, ft.colors.BLUE_500, ft.colors.BLUE_900]
    ]

    example1 = ft.Column([
        ft.Row([
            create_container(str(i*3 + j + 1), colors[i][j])
            for j in range(3)
        ])
        for i in range(3)
    ])

    example2 = ft.Row([
        ft.Column([           
            create_container(str(i*3 + j + 1), colors[i][j])
            for j in range(3)
        ])
        for i in range(3)
    ])

    container = ft.Container(
        ft.Column([
            ft.Text("範例 1 - Row:"),
            example1,
            ft.Divider(),
            ft.Text("範例 2- Column:"),
            example2,
        ])
    )
    
    page.add(container)

ft.app(target=main)
