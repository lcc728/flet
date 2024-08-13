# Flet - Image
# 2024-08-13
# 
import flet as ft

def main(page: ft.Page):   

    page.add(
        ft.Image(src="./image/DSCN1573.jpg", width=200),
        ft.Image(src="./image/IMG_0607.jpg", width=200, border_radius=30),
        ft.Image(src="./image/IMG_0607.jpg", width=200, color=ft.colors.AMBER, color_blend_mode = ft.BlendMode.HARD_LIGHT),
        ft.Image(src="./IMG_0609.jpg", 
                 width=200, 
                 error_content=ft.Text("!!!Error!!!", color=ft.colors.RED)),
    )
    
ft.app(target=main)  
