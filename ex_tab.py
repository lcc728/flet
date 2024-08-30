# Flet - Tab 
# 2024-08-30
# https://www.george.tw/2024/08/30/flet-tab/ 
import flet as ft

def main(page: ft.Page):

    t = ft.Tabs(
        selected_index=1,
        animation_duration=500,
        divider_color= "red",
        divider_height=2,      
        mouse_cursor="TEXT",       
        overlay_color = "yellow",
        unselected_label_color = "amber",
        indicator_border_side=ft.BorderSide(width=10, color=ft.colors.BLUE),  # indicator_color="green",
        indicator_border_radius=10,
        indicator_padding=3,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )
    page.add(t)

ft.app(target=main)
