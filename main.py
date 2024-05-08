from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex

class NewWindow(BoxLayout):
    def __init__(self,):
        pass

class Login(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = ("#DCDCDC")
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        login_label = Label(text="LOGIN", font_size=30, font_name='Georgia', color=get_color_from_hex('#4F4F4F'))
        login_label.valign = 'middle'
        login_label.halign = 'center'

        self.add_widget(login_label)

        # Add an image below the login label
        image = Image(source=r"C:\Users\aluno.sesipaulista\Pictures\R.png", allow_stretch=True)
        image.size_hint = (1, 2.5)  # adjust the size_hint to fit your needs
        self.add_widget(image)

        self.username_input = TextInput(hint_text="Nome de usuário...")
        self.senha_input = TextInput(hint_text="Digite sua senha...", password=True)

        self.add_widget(Label(text="Nome de usuário:", font_name="Arial", color=get_color_from_hex('#4F4F4F')))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#4F4F4F')))
        self.add_widget(self.senha_input)

        self.cadastrar_button = Button(text="Entrar", background_color=(0, 1, 0, 0.75))
        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=('#6A5ACD'))
        self.login_button.on_release = self.on_Tela_Cadastro
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

    def on_Tela_Cadastro(self, instance):
        # Your code here
        pass

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()