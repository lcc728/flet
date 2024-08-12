# Flet - Text
# 2024-08-12
#

import flet as ft

def main(page: ft.Page):

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TAG_FACES),
        leading_width=40,
        title=ft.Text("Text Example"),
        center_title=False,
        bgcolor=ft.colors.LIGHT_BLUE_ACCENT_200,
        toolbar_height= 40,
       
        actions=[
            ft.IconButton(ft.icons.CAKE),
            ft.IconButton(ft.icons.COOKIE_OUTLINED),
            ft.IconButton(ft.icons.BAKERY_DINING_OUTLINED),
       ],     
    )
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "Chewy": "https://github.com/google/fonts/raw/main/apache/chewy/Chewy-Regular.ttf",
    }
    # Font-family  - Kanit  
    font1 = ft.Text(
        "Hello Kanit ",
        size=30,
        font_family="Kanit",
        color = ft.colors.YELLOW_500,        
        bgcolor=ft.colors.GREEN_ACCENT,

    )     
    # Font-family  - RobotoSlab  
    font2 = ft.Text(
        "Hello RobotoSlab",
        size=30,
        font_family="RobotoSlab",
        italic= True,
        color = ft.colors.GREEN_ACCENT_700
    )      
    # Font-family  - Chewy  
    font3 = ft.Text(
        "Hello Chewy ",

        style=ft.TextStyle(
            color=ft.colors.CYAN_500,             
            size=30, 
            font_family="Chewy",
            decoration=ft.TextDecoration.UNDERLINE,
            decoration_color=ft.colors.RED,
            decoration_style=ft.TextDecorationStyle.WAVY,            
        )        
    )    

    font4 = ft.Text(
        "Hello World",
        size=30,
        font_family="Bradley Hand ITC",
        weight=ft.FontWeight.W_300,
        color = ft.colors.RED_500
    )    
  
    page.add(font1,font2,font3,font4)

ft.app(target=main)
