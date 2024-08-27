# Flet temperature conversion
# 2024-08-20 
# https://www.george.tw/2024/08/20/flet-temperature_conversion/

import flet as ft

def main(page: ft.Page):
    page.title = "溫度轉換 Temperature Converter"
    

    def convert(e):
        try:
            if temp_input.value:
                temp = float(temp_input.value)
                if radio_group.value == "c2f":
                    result = (temp * 9/5) + 32
                    result_text.value = f"{temp}°C = {result:.2f}°F"
                else:
                    result = (temp - 32) * 5/9
                    result_text.value = f"{temp}°F = {result:.2f}°C"
                temp_input.value =''
                page.update()
        except ValueError:
            result_text.value = "請輸入數字 !!!"
            temp_input.value =''
            page.update()

    temp_input = ft.TextField(label="請輸入溫度")
    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="c2f", label="攝氏 -> 華式"),
            ft.Radio(value="f2c", label="華氏 -> 攝式")
        ]),
        value="c2f"
    )
    convert_button = ft.ElevatedButton("轉換", on_click=convert)
    result_text = ft.Text('', size=30, color="red")

    page.add(
        ft.Column(
            [
                temp_input,
                radio_group,
                convert_button,
                result_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
