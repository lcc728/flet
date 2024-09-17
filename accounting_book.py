# Flet - Accounting book - 記帳簿
# 2024-09-17
# 

import flet as ft
import csv
from datetime import datetime, date, timedelta
import pandas as pd

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()

    def load_data(self):
       
        try:
            df = pd.read_csv(self.file_path, header=None, names=['日期', '類型', '分類', '描述', '金額'])
            df['日期'] = pd.to_datetime(df['日期'])
            df['收入'] = df.apply(lambda x: x['金額'] if x['類型'] == '收入' else 0, axis=1)
            df['支出'] = df.apply(lambda x: x['金額'] if x['類型'] == '支出' else 0, axis=1)
            df = df.sort_values(by='日期', ascending=False)  
            return df
        except Exception as e:
            print(f"讀取 CSV 檔案時出錯: {e}")
            return pd.DataFrame()  

    def save_entry(self, transaction_type, catalog, summary, amount, date):
       
        with open(self.file_path, mode="a", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date, transaction_type, catalog, summary, amount])
        self.df = self.load_data()  

    def get_data(self):        
        return self.df
    
    def get_expense_statistics(self):
        df = self.df[self.df['類型'] == '支出']
        statistics = df.groupby('分類')['金額'].sum().reset_index()
        return statistics

class PageController:
    def __init__(self, csv_handler, page):
        self.csv_handler = csv_handler
        self.page = page
        self.financial_data_table = None
        self.display_data_table = None
        self.transaction_type = None
        self.catalog = None
        self.summary = None
        self.amount = None
        self.select_date = None

    def create_data_row(self, row):
        
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(row['日期'].strftime('%Y-%m-%d'))),
                ft.DataCell(ft.Text(row['類型'])),
                ft.DataCell(ft.Text(row['分類'])),
                ft.DataCell(ft.Text(row['描述'])),
                ft.DataCell(ft.Text(str(row['收入']), style=ft.TextStyle(color='green' if row['收入'] > 0 else 'black'))),
                ft.DataCell(ft.Text(str(row['支出']), style=ft.TextStyle(color='red' if row['支出'] > 0 else 'black'))),
            ]
        )

    def update_data_table(self, data_table, filtered_df):
        data_table.rows.clear()
        total_income = filtered_df['收入'].sum()
        total_expense = filtered_df['支出'].sum()
        data_table.rows.extend([self.create_data_row(row) for _, row in filtered_df.iterrows()])
        data_table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('總計')),
                    ft.DataCell(ft.Text('')),
                    ft.DataCell(ft.Text('')),
                    ft.DataCell(ft.Text('')),
                    ft.DataCell(ft.Text(str(total_income))),
                    ft.DataCell(ft.Text(str(total_expense)))
                ]
            )
        )
        self.page.update()

    def refresh_data(self, e):
        df = self.csv_handler.load_data()
        self.update_data_table(self.financial_data_table, df)

    def save_entry(self, e):
        self.csv_handler.save_entry(self.transaction_type.value, self.catalog.value, self.summary.value, self.amount.value, self.select_date.value)
        self.summary.value = ""
        self.amount.value = ""
        self.update_data_table(self.display_data_table, self.csv_handler.get_data())

    def create_financial_page(self):
        df = self.csv_handler.get_data()
        if df.empty:
            return ft.Column()  

        month_selector = ft.Dropdown(
            value=str(date.today().month),
            options=[ft.dropdown.Option(str(month)) for month in range(1, 13)],
            label='選擇月份',
            on_change=lambda e: self.filter_data(e.control.value)
        )
        transaction_type_selector = ft.Dropdown(
            options=[
                ft.dropdown.Option("全部"),
                ft.dropdown.Option("收入"),
                ft.dropdown.Option("支出")
            ],
            label='選擇類型',
            value="全部",
            on_change=lambda e: self.filter_data(month_selector.value, e.control.value)
        )
        self.financial_data_table = ft.DataTable(
            sort_column_index=0,
            sort_ascending=True,
            columns=[
                ft.DataColumn(ft.Text('日期')),
                ft.DataColumn(ft.Text('收/支')),
                ft.DataColumn(ft.Text('類型')),
                ft.DataColumn(ft.Text('描述')),
                ft.DataColumn(ft.Text('收入')),
                ft.DataColumn(ft.Text('支出')),
            ],
            rows=[]
        )
      
        self.update_data_table(self.financial_data_table, df)
        refresh_btn = ft.ElevatedButton("更新", on_click=self.refresh_data)
        return ft.Column([month_selector, transaction_type_selector, self.financial_data_table, refresh_btn])

    def filter_data(self, selected_month, transaction_type=None):
        df = self.csv_handler.get_data()
        filtered_df = df[df['日期'].dt.month == int(selected_month)]
        if transaction_type != "全部" :
            filtered_df = filtered_df[filtered_df['類型'] == transaction_type]
        self.update_data_table(self.financial_data_table, filtered_df)

    def display_page(self):
        self.page.title = "記帳"
        today = date.today()
        d1 = today - timedelta(days=90)
        d2 = today + timedelta(days=365)
        date_picker = ft.DatePicker(
            first_date=d1,
            last_date=d2
        )
        self.page.overlay.append(date_picker)

        def date_picker_changed(e):
            self.select_date.value = date_picker.value.strftime("%Y-%m-%d")
            self.select_date.update()

        date_picker.on_change = date_picker_changed

        def open_date_picker(e):
            date_picker.pick_date()

        self.transaction_type = ft.Dropdown(
            label="支出/收入",
            value="支出",
            options=[
                ft.dropdown.Option("支出"),
                ft.dropdown.Option("收入"),
            ]
        )
        self.catalog = ft.Dropdown(
            label="類型",
            value="食",
            options=[
                ft.dropdown.Option("食"),
                ft.dropdown.Option("衣"),
                ft.dropdown.Option("住"),
                ft.dropdown.Option("行"),
                ft.dropdown.Option("育"),
                ft.dropdown.Option("樂"),
                ft.dropdown.Option("其它"),
            ]
        )
        self.summary = ft.TextField(label="費用摘要")
        self.amount = ft.TextField(label="金額", keyboard_type=ft.KeyboardType.NUMBER)
        self.select_date = ft.TextField(label="日期", value=datetime.now().strftime("%Y-%m-%d"))
        rows = ft.Row([
            self.select_date,
            ft.ElevatedButton("選擇日期", on_click=open_date_picker)
        ])

        save_button = ft.ElevatedButton("存檔", on_click=self.save_entry)

        self.display_data_table = ft.DataTable(
            sort_column_index=0,
            sort_ascending=True,
            columns=[
                ft.DataColumn(ft.Text('日期')),
                ft.DataColumn(ft.Text('收/支')),
                ft.DataColumn(ft.Text('類型')),
                ft.DataColumn(ft.Text('描述')),
                ft.DataColumn(ft.Text('收入')),
                ft.DataColumn(ft.Text('支出')),
            ],
            rows=[]
        )

        return ft.Column([self.transaction_type, self.catalog, self.summary, self.amount, rows, save_button])

    def create_statistics_page(self):
            statistics = self.csv_handler.get_expense_statistics()
            if statistics.empty:
                return ft.Column(ft.Text("沒有支出資料"))
            colors = [
                ft.colors.RED,
                ft.colors.GREEN,
                ft.colors.BLUE,
                ft.colors.ORANGE,
                ft.colors.PURPLE,
                ft.colors.YELLOW,
                ft.colors.CYAN,
            ]
            normal_border = ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE))
            hovered_border = ft.BorderSide(6, ft.colors.WHITE)            
            pie_chart_data = [
            ft.PieChartSection(
                    value=row['金額'],
                    title=row['分類'],
                    color=colors[index % len(colors)],
                    radius=150,
                ) for index, row in statistics.iterrows()
            ]
            def on_chart_event(e: ft.PieChartEvent):
                for idx, section in enumerate(pie_chart.sections):
                    section.border_side = (
                        hovered_border if idx == e.section_index else normal_border
                    )
                pie_chart.update()
            pie_chart = ft.PieChart(
                sections=pie_chart_data,
                sections_space=1,
                center_space_radius=0,
                on_chart_event=on_chart_event,
            )

            return ft.Column([ft.Text("消費統計 - 支出部分"), pie_chart])

def main(page: ft.Page):
    csv_handler = CSVHandler('records.csv')  
    page_controller = PageController(csv_handler, page)   
    page.scroll = ft.ScrollMode.AUTO 
    def on_nav_change(e):
        nonlocal page_view
        page_view.controls.clear()        
        if e.control.selected_index == 0:
            page_view.controls.append(page_controller.display_page())
        elif e.control.selected_index == 1:
            page_view.controls.append(page_controller.create_financial_page())
        elif e.control.selected_index == 2:
            page_view.controls.append(page_controller.create_statistics_page())
        page.update()
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.ADD, label="記錄帳務"),
            ft.NavigationBarDestination(icon=ft.icons.LIST, label="顯示帳務"),
            ft.NavigationBarDestination(icon=ft.icons.PIE_CHART_SHARP, label="帳數圖表"),

        ],
        on_change=on_nav_change
    )
    page_view = page_controller.display_page()    
    page.add(page_view, nav_bar)

ft.app(target=main)
