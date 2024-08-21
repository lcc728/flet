# Flet - Container
# 2024-08-21
# https://www.george.tw/2024/08/22/flet-container/

import flet as ft

def main(page: ft.Page):
    page.title = "容器",
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
    page.add(
        ft.Container(
            image_src='102.jpg',
            image_fit=ft.ImageFit.FILL,
            content=ft.Text("This is a container", weight=ft.FontWeight.BOLD,color="white"),
            alignment= ft.alignment.center,
            bgcolor=ft.colors.BLUE_400,
            height=400,
            width=600,
            border_radius=ft.border_radius.all(35),
  
         )
    )

ft.app(target=main)
