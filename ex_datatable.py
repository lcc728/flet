# Flet - DataTable
# 2024-08-23
# https://www.george.tw/2024/08/24/flet-datatable/
import flet as ft

def main(page: ft.Page):
    page.title = "Data Table"
    page.add(
        ft.DataTable(
            width=600,
            bgcolor=ft.colors.CYAN_50, 
            border=ft.border.all(2,"Blue"),
            border_radius=10,
            horizontal_lines=ft.BorderSide(1, "pink"),
            vertical_lines= ft.BorderSide(1, "pink"),
            data_row_color= ft.colors.BLUE_300,
            heading_row_color = ft.colors.YELLOW_100,
            columns=[
                ft.DataColumn(ft.Text("姓名")),
                ft.DataColumn(ft.Text("電話")),
                ft.DataColumn(ft.Text("地址"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("張三")),
                        ft.DataCell(ft.Text("0912-...-...")),
                        ft.DataCell(ft.Text("台北市...")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("李四")),
                        ft.DataCell(ft.Text("0987-...-...")),
                        ft.DataCell(ft.Text("新北市...")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("王五")),
                        ft.DataCell(ft.Text("0921-...-...")),
                        ft.DataCell(ft.Container(content= ft.Text("台中市..."), alignment=ft.alignment.center)),
                    ],
                ),
            ],
        ),
    )

ft.app(target=main)
