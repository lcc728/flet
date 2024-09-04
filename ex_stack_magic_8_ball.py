# Flet - Stack - 神奇 8 號球
# 2024-09-04
# https://www.george.tw/2024/09/05/flet-stack-%e7%a5%9e%e5%a5%878%e8%99%9f%e7%90%83/

import flet as ft 
import random

MagicMap = {
            1:'It is certain \n這是必然',
            2:'It is decidedly so \n肯定是的',
            3:'Without a doubt  \n不用懷疑',
            4:'Yes, definitely  \n毫無疑問',
            5:'You may rely on it  \n你能依靠它',
            6:'As I see it, yes  \n如我所見，是的',
            7:'Most likely  \n很有可能',
            8:'Outlook good  \n外表很好',
            9:'Yes  \n是的',
            10:'Signs point to yes  \n種種跡象指出「是的」',
            11:'Reply hazy try again  \n回覆攏統，再試試',
            12:'Ask again later  \n待會再問',
            13:'Better not tell you now  \n最好現在不告訴你',
            14:'Cannot predict now  \n現在無法預測',
            15:'Concentrate and ask again  \n專心再問一遍',
            16:'Don\'t count on it  \n想的美',
            17:'My reply is no  \n我的回覆是「不」',
            18:'My sources say no  \n我的來源說「不」',
            19:'Outlook not so good \n外表不太好',
            20:'Very doubtful  \n很可疑'
        }

def main(page:ft.page):
    page.title= "神奇8號球"
    page.window.width = 480
    page.window.height= 600

    def magic_ball(e): 
        magicNum = random.randint(1,20)
        result_text.value = MagicMap[magicNum]
        result_text.update()


    result_text = ft.Text(
                    "在下面輸入你的問題\n       按下送出鈕 \n   我可以幫你解答",
                    color="white",
                    size=20,
                    weight="bold",
                    opacity=0.4,
                )
    st = ft.Stack(
        [
            ft.Image(
                src="./8.png",
                width=450,
                height=450,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Container(
                content=result_text,
                alignment=ft.alignment.center,
            ),
        ],
        width=450,
        height=450,
        )
    question_input = ft.TextField(label="問題")
    answer_button = ft.ElevatedButton("送出", on_click=magic_ball)
    page.add(st, question_input, answer_button)

ft.app(target=main)
