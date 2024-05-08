from kivy.app import App 
from kivy.uix.boxlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        # layout principal 
        layout_principal = GridLayout(colos=2)

        # Coluna à esquerda (30% da tela)
        coluna_esquerda = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        menu_itens = ['Arquivo', 'Editar', 'Eleção', 'Ver', 'Acessar', 'Sair']
        label11 = Label(text='Menu')
        coluna_esquerda.add_widget(label11)

        for item in menu_itens:
            botao = Button(text=item)
            coluna_esquerda.add_widget(label11)
        for item in menu_itens:
            botao = Button(text=item)
            coluna_esquerda.add_widget(botao)

        # Coluna à direira dividida em três partes iguais
        coluna_direita = GridLayout(cols=1, rows=3)
        for i in range(3):
            botao = Button(text=f'Botão {i+7}')
            coluna_direita.add_widget(botao)

        # Adicionando as colunas ao layout principal
        layout_principal.add_widget(coluna_esquerda)
        layout_principal.add_widget(coluna_direita)

        return layout_principal
                
if __name__ == "__main__":
    MinhaApp().run()
