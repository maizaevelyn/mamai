from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        Label(text='Olá,SENAI',
              halign='left', #Alinha o texto à esquerda
              valign='top',   #Alinha o texto no topo
              size_hint=(None, None), #Desativa o ajuste automático do tamanho
              size=(150, 50), #Define a largua máxima do texto
        )
