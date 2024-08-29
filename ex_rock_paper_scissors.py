# Flet - Rock paper scissors - 剪刀石頭布 
# 2024-08-29
# https://www.george.tw/2024/08/30/flet-rock-paper-scissors/
import flet as ft
import random

def main(page: ft.Page):
    page.title = "剪刀石頭布遊戲"

    result_text = ft.Row([ft.Text("請出拳")], alignment=ft.MainAxisAlignment.CENTER)
    score_text = ft.Text(size=16, text_align=ft.TextAlign.CENTER)
    player_score = 0
    computer_score = 0

    def play_game(player_choice):
        nonlocal player_score, computer_score
        choices = [ft.icons.CONTENT_CUT, ft.icons.CIRCLE, ft.icons.BACK_HAND_SHARP]
        computer_choice = random.choice(choices)
        
        result = ""
        if player_choice == computer_choice:
            result = "平手，再試一次吧!"
        elif (
            (player_choice == ft.icons.CONTENT_CUT and computer_choice ==  ft.icons.BACK_HAND_SHARP) or
            (player_choice == ft.icons.CIRCLE and computer_choice == ft.icons.CONTENT_CUT) or
            (player_choice == ft.icons.BACK_HAND_SHARP and computer_choice == ft.icons.CIRCLE)
        ):
            result = "你贏了!"
            player_score += 1
        else:
            result = "你輸了!"
            computer_score += 1
        
        result_text.controls = [
            ft.Text("你出 "),
            ft.Icon(player_choice, color="red"),
            ft.Text(", 電腦出 "),
            ft.Icon(computer_choice, color="green"),
            ft.Text(f". {result}")
        ]
        score_text.value = f"你贏 {player_score} 次- 輸 {computer_score} 次"
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(icon=ft.icons.CONTENT_CUT, on_click=lambda _: play_game(ft.icons.CONTENT_CUT), icon_size=50),
            ft.IconButton(icon=ft.icons.CIRCLE, on_click=lambda _: play_game(ft.icons.CIRCLE), icon_size=50),
            ft.IconButton(icon=ft.icons.BACK_HAND_SHARP, on_click=lambda _: play_game(ft.icons.BACK_HAND_SHARP), icon_size=50),
        ], alignment=ft.MainAxisAlignment.CENTER),
        result_text,
        score_text,
    )

ft.app(target=main)
