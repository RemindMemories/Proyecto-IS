import flet as ft
from flet import Page
from flet import TextField, ElevatedButton, Text, Column, ControlEvent, Container, alignment

def show_main_app(page: Page, username: str, go_back):
        page.title = 'Aplicación Principal'
        page.clean()

        def logout(e):
            page.clean()
            go_back()

        selected_section = Text("Seleccione una opcion ;P", size=16, weight="bold")
        
        def navigate_to_section(section: str):
            selected_section.value = f"{section}"
            page.update()

        def style_button(text,icon,on_click, color=None):
            return Container(
                content=ElevatedButton(text, icon=icon, on_click=on_click, color=color),
                padding=10,
                bgcolor=ft.Colors.BLUE_50,
                border_radius=10,
            )


        nav_buttons = Column([
            ft.Divider(height=80, color="transparent"),
            style_button(
                text="Home",
                icon=ft.Icons.HOME, 
                on_click=lambda e: navigate_to_section("Home 🏠​")
                ),
            style_button(
                text="Buscar libros",
                icon=ft.Icons.SEARCH, 
                on_click=lambda e: navigate_to_section("Buscar libros 🔎​")),
            style_button(text="Mis libros",
                         icon=ft.Icons.BOOK, 
                         on_click=lambda e: navigate_to_section("Mis libros 📚​")),         
            style_button(text="Cerrar sesión",
                            icon=ft.Icons.LOGOUT,
                         color = "red", on_click=logout)
        ],
        spacing=10
        )

        title = ft.Row([
            Container(
                 content=Text(f"Bienvenid@, {username}! 🦉​", size=24, weight="bold"),
                 padding=20,
                 bgcolor=ft.Colors.BLUE_50,
                 expand=True,
            )    
        ])

        content = Column([
            Container(selected_section),
        ], expand=True)

        page.add(
             ft.Row(
                  controls=[
                      Container(nav_buttons, width=190, padding=10, bgcolor=ft.Colors.BLUE_50, border_radius=10),
                      ft.VerticalDivider(width=1),
                      Column(
                           controls=[
                                Container(title, bgcolor=ft.Colors.BLUE_50),
                                ft.Divider(height=1),
                                Container(content, expand=True)
                           ],
                           expand=True,
                      )
                  ],
                  expand=True,
             )
        )

        def show_search_books(e):
            page.clean()
            search_text = TextField(label='Buscar libros', width=200)
            search_button = ElevatedButton("Buscar", on_click=lambda e: search_books(search_text.value))
            message = Text("", color="red")

            def search_books(query):
                # Aquí iría la lógica para buscar libros
                message.value = f"Buscando libros con '{query}'..."
                page.update()

            content = Column([
                Text("Buscar libros", size=24, weight="bold"),
                search_text,
                search_button,
                message
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)

            page.add(Container(content=content, alignment=alignment.center, expand=True))

