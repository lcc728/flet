# Flet -QR Code Generator
# 2024-08-16 
# https://www.george.tw/2024/08/17/flet-qrcode-generator/
import flet as ft
import qrcode
import os
import time

def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN_400,
          
        )
    )    
    textField = ft.TextField(
        label="請輸入文字", 
        border=ft.InputBorder.UNDERLINE, 
    )
    image = ft.Image(src="123.png")
    textOutput = ft.Text(" ", color="blue")

    def generate_qrcode(e):
        text = textField.value
        img = qrcode.make(text)        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        timestamp = int(time.time())  
        qr_filename = f"qrcode_{timestamp}.png"
        qr_path = os.path.join(current_dir, qr_filename)        
        img.save(qr_path)     
        image.src = qr_path
        textOutput.value = f"此圖的文字容為: {textField.value}"
        page.update()
        time.sleep(0.1)
        os.remove(qr_path )

    button = ft.ElevatedButton(text="產生 QR Code", icon=ft.icons.QR_CODE_2_ROUNDED, on_click=generate_qrcode)
    page.add( textField, button, image , textOutput)

ft.app(target=main)
