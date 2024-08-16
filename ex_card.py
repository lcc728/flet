# Flet - Card
# 2024-08-16
# https://www.george.tw/2024/08/17/flet-card/
import flet as ft

def main(page: ft.Page):
    card1 = ft.Card(
        content=ft.Text("      CARD 1 "),
        width=300,
        height=200,
        margin=16,
        color="blue",
        elevation=10, 
        shadow_color = "red",
        
        shape=ft.RoundedRectangleBorder(ft.border_radius.all(15)),
    )
    card2 = ft.Card(
        content=ft.Text("   CARD 2 "),
        width=300,
        height=200,
        margin=30,
        color="green",
        elevation=20, 

        shape=ft.BeveledRectangleBorder(ft.border_radius.all(15)),
    )    
    page.add(card1, card2)

ft.app(target=main)
