import flet as ft

def main(page: ft.Page):
    page.title = "Meu App Flet"
    page.add(ft.Text("Olá, Flet!"))

ft.app(target=main)
