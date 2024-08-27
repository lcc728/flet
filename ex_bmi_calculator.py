# Flet - BMI Calculator 
# 2024-08-22 
# https://www.george.tw/2024/08/22/flet-bmi-calculator/
import flet as ft

def main(page: ft.Page):
    page.title = "BMI 計算"

    def calculate_bmi(e):
        try:
            weight = float(weight_input.value)
            height = float(height_input.value)
          
            if height_unit.value == "英呎":
                height *= 30.48  
            if weight_unit.value == "磅":
                weight *= 0.454  

            bmi = weight / ((height / 100) ** 2)  
          
            if bmi <=18.5:
                color = "blue"
                report = "太輕"
            elif bmi > 24:
                color = "red"
                report = "過胖"
            else:
                color ="green"
                report = "標準"

            result_text.value = f" {bmi:.2f} - {report}"
            result_text.color = color
            
        except ValueError:
            result_text.value = "請輸入數字"
            result_text.color = "black"
        page.update()    
        
    weight_input = ft.TextField(label="體重", keyboard_type=ft.KeyboardType.NUMBER , width=100)
    weight_unit = ft.RadioGroup(
        value="公斤",
        content=ft.Row([
            ft.Radio(value="公斤", label="公斤"),
            ft.Radio(value="磅", label="磅")
        ]),
        
    )
    weight_row = ft.Row([
        weight_input,
        weight_unit 
    ])   

    height_input = ft.TextField(label="身高", keyboard_type=ft.KeyboardType.NUMBER, width=100)
    height_unit = ft.RadioGroup(
        value="公分",
        content=ft.Row([
            ft.Radio(value="公分", label="公分"),
            ft.Radio(value="英呎", label="英呎")
        ]),
        
    )
    height_row = ft.Row([
        height_input,
        height_unit 
    ])   
        
    calculate_button = ft.ElevatedButton("計算 BMI", on_click=calculate_bmi)
    result_text = ft.Text('', color='black')
    rows = ft.Row([
        ft.Text("您的 BMI 是:"),
        result_text 

    ])
  

    page.add(weight_row, height_row, calculate_button, rows)

ft.app(target=main)
