from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        # Create a background image
        self.background_image = Image(source=r"C:\Users\aluno.sesipaulista\Desktop\login\imagens e icones\download.jpg", allow_stretch=True)
        self.background_image.size_hint = (1, 1)
        self.add_widget(self.background_image)

        # Create a layout to hold the other widgets
        self.content_layout = BoxLayout(orientation="vertical")
        self.add_widget(self.content_layout)

        self._create_widgets()

    def _create_widgets(self):
        login_label = Label(text="LOGIN", font_size=30, font_name='Georgia', color=get_color_from_hex('#4F4F4F'))
        login_label.valign = 'middle'
        login_label.halign = 'center'
        self.add_widget(login_label)

        image = Image(source=r"C:\Users\aluno.sesipaulista\Pictures\R.png", allow_stretch=True)
        image.size_hint = (1, 2.5)
        self.add_widget(image)

        form_grid = GridLayout(cols=2, spacing=10)
        self.add_widget(form_grid)

        form_grid.add_widget(Label(text="Nome de usuário:", font_name="Arial", color=get_color_from_hex('#4F4F4F')))
        self.username_input = TextInput(hint_text="Nome de usuário...")
        form_grid.add_widget(self.username_input)

        form_grid.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#4F4F4F')))
        self.senha_input = TextInput(hint_text="Digite sua senha...", password=True)
        form_grid.add_widget(self.senha_input)

        button_grid = GridLayout(cols=2, spacing=10)
        self.add_widget(button_grid)

        self.cadastrar_button = Button(text="Entrar", background_color=(0, 1, 0, 0.75))
        button_grid.add_widget(self.cadastrar_button)

        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=('#6A5ACD'))
        self.login_button.on_release = self.on_tela_cadastro
        button_grid.add_widget(self.login_button)

    def on_tela_cadastro(self):
        self.clear_widgets()
        self.add_widget(RegisterScreen())

class RegisterScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 50]
        self.spacing = 20

        # Create a background image
        self.background_image = Image(source=r"C:\Users\aluno.sesipaulista\Pictures\background_image.png", allow_stretch=True)
        self.background_image.size_hint = (1, 1)
        self.add_widget(self.background_image)

        # Create a layout to hold the other widgets
        self.content_layout = BoxLayout(orientation="vertical")
        self.add_widget(self.content_layout)

        self._create_widgets()

    def _create_widgets(self):
        register_label = Label(text="REGISTRO", font_size=30, font_name='Georgia', color=get_color_from_hex('#4F4F4F'))
        register_label.valign = 'middle'
        register_label.halign = 'center'
        self.add_widget(register_label)

        form_grid = GridLayout(cols=2, spacing=10)
        self.add_widget(form_grid)

        form_grid.add_widget(Label(text="Nome:", font_size=18, font_name="Arial", color=get_color_from_hex('#4F4F4F')))
        self.nome_input = TextInput(hint_text="Nome...", font_size=16)
        form_grid.add_widget(self.nome_input)

        form_grid.add_widget(Label(text="Data de Nascimento:", font_size=18, font_name="Arial", color=get_color_from_hex('#4F4F4F')))
        self.data_nascimento_input = TextInput(hint_text="DD/MM/YYYY...", font_size=16)
        form_grid.add_widget(self.data_nascimento_input)

        form_grid.add_widget(Label(text="CPF:", font_size=18, font_name="Arial", color=get_color_from_hex('#4F4F4F')))
        self.cpf_input = TextInput(hint_text="CPF...", font_size=16)
        form_grid.add_widget(self.cpf_input)

        form_grid.add_widget(Label(text="RG:", font_size=18, font_name="Arial", color=get_color_from_hex('#4F4F4F')))
        self.rg_input = TextInput(hint_text="RG...", font_size=16)
        form_grid.add_widget(self.rg_input)

        button_grid = GridLayout(cols=1, spacing=10)
        self.add_widget(button_grid)

        self.register_button = Button(text="Cadastrar", background_color=(0, 1, 0, 0.75), font_size=18)
        button_grid.add_widget(self.register_button)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()