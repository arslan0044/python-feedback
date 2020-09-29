import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    #some widgets added here
    name = ObjectProperty(None)
    experience = ObjectProperty(None)
    stars = ObjectProperty(None)

    def submit_btn(self):
        print("Name: ", self.name.text, "Your Experience: ", self.experience.text, "Stars: ", self.stars.text)

        #empty strings after clicking submit
        self.name.text = ""
        self.experience.text = ""
        self.stars.text = ""


#just dont touch this
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
