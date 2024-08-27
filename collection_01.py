# Flet - Tab - 練習集 - QR Code, Password 產生器, BMI 計算機, 溫度轉換器
# 2024-08-27
# 

import flet as ft
import qrcode
import os
import random
import string

def main(page: ft.Page):

    page.title = "Flet 練習集"

    def generate_qr_code(e):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        text = qr_text.value
        qr.add_data(qr_text.value)
        qr.make(fit=True)
        img = qrcode.make(text)    
        current_dir = os.path.dirname(os.path.abspath(__file__))
        qr_filename = f"qrcode.png"
        qr_path = os.path.join(current_dir, qr_filename)        
        img.save(qr_path)     
        qr_image.src = qr_path
        qr_image.update()

    def generate_password(e):
        length = int(password_length.value)
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        password_result.value = password
        password_result.update()

    def calculate_bmi(e):
        try:
            weight = float(weight_input.value)
            height = float(height_input.value)
            bmi = weight / ((height / 100) ** 2)  
            color, report = determine_bmi_category(bmi)
            bmi_result.value = f" {bmi:.2f} - {report}"
            bmi_result.color = color

        except ValueError:
            bmi_result.value = "請輸入數字"
            bmi_result.color = "black"
        bmi_result.update()  

    def determine_bmi_category(bmi):
        if bmi <= 18.5:
            return "blue", "太輕"
        elif bmi < 24:
            return "green", "標準"
        else:
            return "red", "過胖"  

    def convert(e):
        try:
            if temp_input.value:
                temp = float(temp_input.value)
                if radio_group.value == "c2f":
                    result = (temp * 9/5) + 32
                    temp_result.value = f"{temp}°C = {result:.2f}°F"
                else:
                    result = (temp - 32) * 5/9
                    temp_result.value = f"{temp}°F = {result:.2f}°C"
                temp_input.value =''
                temp_result.update()
        except ValueError:
            temp_result.value = "請輸入數字 !!!"
            temp_input.value =''
            temp_result.update()

    qr_text = ft.TextField(label="輸入要生成 QR Code 的文字")
    qr_button = ft.ElevatedButton("生成 QR Code", on_click=generate_qr_code)
    qr_image = ft.Image(src="123456.png")

    password_length = ft.Slider(min=6, max=30, divisions=24, label="{value}", value=16)
    password_button = ft.ElevatedButton("產生密碼", on_click=generate_password)
    password_result = ft.Text()    

    weight_input = ft.TextField(label="體重 kg", keyboard_type=ft.KeyboardType.NUMBER , width=100)
    height_input = ft.TextField(label="身高 cm", keyboard_type=ft.KeyboardType.NUMBER, width=100)
    calculate_button = ft.ElevatedButton("計算 BMI", on_click=calculate_bmi)
    bmi_result = ft.Text('', color='black')
    rows = ft.Row([
        ft.Text("您的 BMI 是:"),
        bmi_result 

    ])   

    temp_input = ft.TextField(label="請輸入溫度")
    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="c2f", label="攝氏 -> 華式"),
            ft.Radio(value="f2c", label="華氏 -> 攝式")
        ]),
        value="c2f"
    )
    convert_button = ft.ElevatedButton("轉換", on_click=convert)
    temp_result = ft.Text('', size=30, color="red")     

    t = ft.Tabs(
        selected_index=2,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="QR Code",
                icon=ft.icons.QR_CODE,
                content=ft.Container(ft.Column([qr_text, qr_button, qr_image]), margin=10),
            ),
            ft.Tab(
                text="密碼",
                icon=ft.icons.PASSWORD,
                content=ft.Container(ft.Column([ft.Text("選擇密碼長度:"), password_length, password_button, password_result]), margin=10),
            ),
            ft.Tab(
                text="BMI",
                icon=ft.icons.SCALE,
                content=ft.Container(ft.Column([ weight_input, height_input, calculate_button, rows]), margin=10),
            ),    
            ft.Tab(
                text="Temperature",
                icon=ft.icons.DEVICE_THERMOSTAT,
                content=ft.Container(ft.Column([temp_input,radio_group,convert_button,temp_result]), margin=10),
            ),                      
        ],
        expand=1,
    )

    page.add(t)

ft.app(target=main)
