import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, ControlEvent


def main(page: ft.Page):
    page.title = 'Pagina de bienvenida'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False


    def show_landing():
        page.clean()
        
        page.add(
            Column([
                Text("Librería Búho {O,O}", size=30, weight="bold"),
                Text("¡La aplicacion que conecta todas las bibliotecas Unison!", size=15),
                text_username := TextField(label='Usuario', width=200),
                text_password := TextField(label='Contraseña', width=200, password=True),
                ElevatedButton("¿No tienes cuenta? Registrate", on_click=lambda e: show_signup()),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )


    def show_signup():
        page.title = "Sign Up"

        text_username = TextField(label='Username', width=200)
        text_password = TextField(label='Password', width=200, password=True)
        checkbox_agree = Checkbox(label='I agree to the terms', value=False)
        button_submit = ElevatedButton(text='Sign Up', width=200, disabled=True)

        def validate(e: ControlEvent):
            button_submit.disabled = not all([text_username.value, text_password.value, checkbox_agree.value])
            page.update()

        def submit(e: ControlEvent):
            print("Signed up:", text_username.value)
            page.clean()
            page.add(Text(f"Thanks for signing up, {text_username.value}!", size=20))

        text_username.on_change = validate
        text_password.on_change = validate
        checkbox_agree.on_change = validate
        button_submit.on_click = submit

        page.clean()
        page.add(
            Column([
                Text("Sign Up", size=24, weight="bold"),
                text_username,
                text_password,
                checkbox_agree,
                button_submit,
                ElevatedButton("Back", on_click=lambda e: show_landing())
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )


    def show_login():
        page.title = "Log In"

        login_user = TextField(label="Username", width=200)
        login_pass = TextField(label="Password", width=200, password=True)
        login_btn = ElevatedButton(text="Log In", width=200)

        def login(e: ControlEvent):
            print("Logged in:", login_user.value)
            page.clean()
            page.add(Text(f"Welcome back, {login_user.value}!", size=20))

        login_btn.on_click = login

        page.clean()
        page.add(
            Column([
                Text("Log In", size=24, weight="bold"),
                login_user,
                login_pass,
                login_btn,
                ElevatedButton("Back", on_click=lambda e: show_landing())
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

    show_landing()


if __name__ == "__main__":
    ft.app(target=main)
