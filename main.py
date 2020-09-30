import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.core.text import LabelBase
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider

Window.clearcolor = (1, 1, 1, 1) #white background

LabelBase.register(name="KeepCalm", #adding the font KeepCalm
    fn_regular= "KeepCalm-Medium.ttf"
    )


#just dont touch this unless you know what you are doing
class MyApp(App):
    def star1(self):
        print("it worked - star 1")

    def star2(self):
        print("it worked - star 2")

    def star3(self):
        print("it worked - star 3")

    def star4(self):
        print("it worked - star 4")

    def star5(self):
        print("it worked - star 5")

    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    MyApp().run()
