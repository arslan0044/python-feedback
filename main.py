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
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv") #this basically defines the kv file that we are using for this screen

LabelBase.register(name="KeepCalm", #adding the font KeepCalm
    fn_regular= "KeepCalm-Medium.ttf"
    )
Window.clearcolor = (1, 1, 1, 1)
Window.size = (1280, 800) #this is usually a resolution used by tablets (the main device i want to use this one)

#just dont touch this unless you know what you are doing
class MyMainApp(App):
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
        return kv

if __name__ == "__main__":
    MyMainApp().run()
