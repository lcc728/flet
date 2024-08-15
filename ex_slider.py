# Flet - Slider
# 2024-05-15
# https://www.george.tw/2024/08/16/flet-slider/
import flet as ft

def main(page: ft.Page):
    page.title = "Slider 測試:"
    def slider_changed(e):
        value = round(e.control.value)
        sliderText.value = f"你選擇的值是:{value}"
        page.update()

    sliderTitle = ft.Text(f"請選擇一個值")
    slider = ft.Slider(
        min=0,
        max=100,
        divisions=50,
        label="請做出選擇",
        on_change=slider_changed
    )
    sliderText = ft.Text(f"你選擇的值是:")
    page.add( sliderTitle , slider,t)

ft.app(target=main)
