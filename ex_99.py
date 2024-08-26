# Flet - Multiplication table - 99 乘法表
# 2024-08-26
# https://www.george.tw/2024/08/26/flet-datatable-multiplication-table/
import flet as ft

def main(page: ft.Page):
    page.title = "99 乘法表"

    dt = ft.DataTable(
        width=800,
        border=ft.border.all(2, "black"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, "black"),
        horizontal_lines=ft.border.BorderSide(1, "black"),
        column_spacing=5,
        heading_row_height=50,
        data_row_max_height=50,
        columns=[
             ft.DataColumn(ft.Container(content=ft.Text("*", size=20, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center)),
             *[ft.DataColumn(ft.Container(content=ft.Text(str(i), size=20, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center,width=72)) for i in range(1, 10)]            
            
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Container(ft.Text(str(i), size=20, weight=ft.FontWeight.BOLD))),
                    *[ft.DataCell(ft.Container(content=ft.Text(str(i*j), size=20, color= "blue"), alignment=ft.alignment.center)) for j in range(1, 10)]
                ]
            ) for i in range(1, 10)
        ]
    )

    page.add(dt)

ft.app(target=main)
