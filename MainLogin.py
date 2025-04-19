import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Column, ControlEvent, Container, alignment
from database_utils import verificar_usuario, agregar_usuario

def main(page: ft.Page):
    page.title = 'Librería Búho {O,O}'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    def show_landing():
        page.clean()

        text_username = TextField(label='Usuario', width=200)
        text_password = TextField(label='Contraseña', width=200, password=True)
        message = Text("", color="red")

        def login(e: ControlEvent):
            if text_username.value and text_password.value:
                success, msg = verificar_usuario(text_username.value, text_password.value)
                if success:
                    page.clean()
                    page.add(Container(
                        content=Text(f"Bienvenido, {text_username.value}!", size=20),
                        alignment=alignment.center,
                        expand=True
                    ))
                else:
                    message.value = msg
                    page.update()
            else:
                message.value = "Por favor, complete todos los campos."
                page.update()

        content = Column(
            [
                Text("Librería Búho {O,O}", size=30, weight="bold"),
                Text("¡Conecta todas las bibliotecas Unison!", size=15),
                text_username,
                text_password,
                ElevatedButton("Iniciar sesión", on_click=login),
                ElevatedButton("¿No tienes cuenta? Regístrate", on_click=lambda e: show_signup()),
                message
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page.add(Container(content=content, alignment=alignment.center, expand=True))

    def show_signup():
        page.clean()

        text_username = TextField(label='Usuario', width=200)
        text_password = TextField(label='Contraseña', width=200, password=True)
        checkbox_agree = Checkbox(label='Acepto los términos', value=False)
        button_submit = ElevatedButton(text='Registrarse', width=200, disabled=True)
        message = Text("", color="red")

        def validate(e: ControlEvent):
            button_submit.disabled = not all([text_username.value, text_password.value, checkbox_agree.value])
            page.update()

        def submit(e: ControlEvent):
            success, msg = agregar_usuario(text_username.value, text_password.value)
            if success:
                page.clean()
                page.add(Container(
                    content=Text(f"Gracias por registrarte, {text_username.value}!", size=20),
                    alignment=alignment.center,
                    expand=True
                ))
            else:
                message.value = msg
                page.update()

        text_username.on_change = validate
        text_password.on_change = validate
        checkbox_agree.on_change = validate
        button_submit.on_click = submit

        content = Column([
            Text("Registrarse", size=24, weight="bold"),
            text_username,
            text_password,
            checkbox_agree,
            button_submit,
            ElevatedButton("Volver", on_click=lambda e: show_landing()),
            message
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        page.add(Container(content=content, alignment=alignment.center, expand=True))

    show_landing()

if __name__ == "__main__":
    ft.app(target=main)
