from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Label(text='Olá,SENAI!', font_size=10,font_name='Arial',color=get_color_from_hex('#FF5733'))
    
if __name__=="_main_":
     MinhaApp().run()
