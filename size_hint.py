from kivy.app import App
from kivy.uix.button import Button 

class MinhaApp(App):
    def build(self):
        return Button(text='Cilque Aqui', size_hint=(0.5, 0.2))
    # Botão ocupará metade da largadura e 20% da altura do layout pai

if __name__ == "__main__":
    MinhaApp().run()
  
