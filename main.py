import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout





#just dont touch this unless you know what you are doing
class MyApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    MyApp().run()
