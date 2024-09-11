# Flet Guess Number - 1A2B - 猜數字遊戲
# 2024-09-11
# https://www.george.tw/2024/09/11/flet-guess-number-1a2b/
import flet as ft
import random

class Game:
  def __init__(self, page, guess_input, result_text):
    self.page = page
    self.guess_input = guess_input
    self.result_text = result_text    
    self.answer = random.sample(range(10), 4)
    self.history_list = ft.ListView(expand=True)

  def start_game(self, e):
    self.answer = random.sample(range(10), 4)
    self.guess_input.disabled = False
    self.history_list.controls.clear()
    self.page.update()

  def check_answer(self, e):
    guess = [int(x) for x in self.guess_input.value]
    a_count = sum(1 for i in range(4) if guess[i] == self.answer[i])
    b_count = sum(1 for i in range(4) if guess[i] in self.answer) - a_count
    self.result_text.value = f"{a_count}A{b_count}B"
    self.history_list.controls.append(ft.Text(f"你的猜測: {self.guess_input.value}, 結果: {a_count}A{b_count}B"))
    
    if a_count == 4:
      self.result_text.value = "恭喜你答對了！"
      self.guess_input.disabled = True
    self.page.update()

def main(page: ft.Page):
  page.window.width = 400
  
  guess_input = ft.TextField(label="請輸入你的猜測")
  result_text = ft.Text()
  game = Game(page, guess_input, result_text)  

  page.add(
      guess_input,
      ft.Row([
          ft.ElevatedButton(text="送出", on_click=game.check_answer),
          ft.ElevatedButton(text="重來", on_click=game.start_game)
      ]),
      result_text,
      game.result_text
  )

ft.app(target=main)
