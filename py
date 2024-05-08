from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label 

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Criando e adicionando um botão com texto, cor de fudo e tamanho de fonte personalizados
        btn1 = Button(text='Botão 1', background_color=(0.2, 0.7, 0.3, 1), font_size=20)
        layout.add_widget(btn1)

        # Criando e adicionando um botão com um texto diferente e alinhamento horizontal personalizado 
        btn2 = Button(text='Clique Aqui!', halign='center')
        layout.add_widget(btn2)

        #criando e adicionando um botão com um texto grande e cor de fundo personalizada
        bnt3 = Button(text='Clique para Continuar', background_color=(0.9, 0.5, 0.1, 1), font_size=30)
        layout.add_widget(bnt3)

        # Criando e adicionando um botão com um ação personalizada ao ser pressionado
        def acao_botao(instance):
            instance.text = 'Botão pressionado!'

        btn4 = Button(text='Botão 4')
        btn4.bind(on_press='Botão 4')
        layout.add_widget(btn4)

        # Adicionando um rótulo para exibir informações adicionais 
        info_label1 = Label(text='pressione os botões para ver diferente propriedades em ação.')
        layout.add_widget(info_label1)

        return layout
        
if __name__ == "__main__":
    MinhaApp().run()
