from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from chart import Jogador
class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.row_force_default = False
        self.row_default_height = 40

        # Defina a altura fixa para o formulário
        self.form_height = 300

        def buttonAdd(aux):
            self.add_widget(Label(text="Atributo  : ", size_hint_x=None, width=100))
            atributo_novo = TextInput(multiline=False)
            self.add_widget(atributo_novo)

        def callFunction(instance):
            # Acesse diretamente os widgets TextInput para obter os valores
            nome = self.name.text
            lastName = self.lastName.text

            try:
                atributo1 = int(self.atributo1.text)
            except ValueError:
                atributo1 = 0

            try:
                atributo2 = int(self.atributo2.text)
            except ValueError:
                atributo2 = 0

            try:
                atributo3 = int(self.atributo3.text)
            except ValueError:
                atributo3 = 0

            try:
                atributo4 = int(self.atributo4.text)
            except ValueError:
                atributo4 = 0


            Jogador(atributo1, atributo2, atributo3, atributo4, nome, lastName)

            if hasattr(self, 'image_widget'):
                # Se a imagem já existe, apenas atualize os atributos
                self.image_widget.source = './yourfile.png'
            else:
                # Crie um novo widget de imagem se ainda não existir
                self.image_widget = Image(
                    source='./yourfile.png',
                    size=(500, 500),
                    size_hint=(None, None),
                    pos=(self.width / 2 , -self.form_height/2))  # Posição abaixo do formulário
                self.add_widget(self.image_widget)

        self.add_widget(Label(text="First Name: ", size_hint_x=None, width=100))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: ", size_hint_x=None, width=100))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Atributo 1 : ", size_hint_x=None, width=100))
        self.atributo1 = TextInput(multiline=False)
        self.add_widget(self.atributo1)

        self.add_widget(Label(text="Atributo 2 : ", size_hint_x=None, width=100))
        self.atributo2 = TextInput(multiline=False)
        self.add_widget(self.atributo2)

        self.add_widget(Label(text="Atributo 3 : ", size_hint_x=None, width=100))
        self.atributo3 = TextInput(multiline=False)
        self.add_widget(self.atributo3)

        self.add_widget(Label(text="Atributo4 : ", size_hint_x=None, width=100))
        self.atributo4 = TextInput(multiline=False)
        self.add_widget(self.atributo4)

        button_generate = Button(text='Gerar Gráfico', font_size=14)
        button_generate.bind(on_press=callFunction)
        self.add_widget(button_generate)


class MeuAplicativo(App):
    def build(self):
        return MyGrid()

MeuAplicativo().run()

