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
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="isaccea"
)

mycursor = mydb.cursor()

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

#global vars
employee1_chosed = False
employee2_chosed = False
employee3_chosed = False
employee4_chosed = False
employee5_chosed = False
employee6_chosed = False
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

        #this is probably the most inefficient code i ever wrote

    employee1 = "Michael"
    employee2 = "John"
    employee3 = "Betty"
    employee4 = "Emily"
    employee5 = "Elizabeth"
    employee6 = "George"

    def employee1_choose(self):
        global employee1_chosed
        employee1_chosed = True
        #set these all to false so only 1 at the time can be chosen
        employee2_chosed = False
        employee3_chosed = False
        employee4_chosed = False
        employee5_chosed = False
        employee6_chosed = False
        print("employee1_choose was set to: " + str(employee1_chosed))

        if employee1_chosed == True:
            print("trying step 2")

            sql = "INSERT INTO feedback (name, stars) VALUES (%s, %s)" #inserting data into the mysql database
            val = ("Michael", "") #going to add stars later
            mycursor.execute(sql, val)

            mydb.commit() #need this to update the db
            print(mycursor.rowcount, "record inserted. step 2 worked")

    def employee2_choose(self):
        global employee2_chosed
        #set these all to false so only 1 at the time can be chosen
        employee1_chosed = False
        employee2_chosed = True
        employee3_chosed = False
        employee4_chosed = False
        employee5_chosed = False
        employee6_chosed = False
        print("employee2_choose was set to: " + str(employee2_chosed))

    def employee3_choose(self):
        global employee3_chosed
        #set these all to false so only 1 at the time can be chosen
        employee1_chosed = False
        employee2_chosed = False
        employee3_chosed = True
        employee4_chosed = False
        employee5_chosed = False
        employee6_chosed = False
        print("employee3_choose was set to: " + str(employee3_chosed))

    def employee4_choose(self):
        global employee4_chosed
       #set these all to false so only 1 at the time can be chosen
        employee1_chosed = False
        employee2_chosed = False
        employee3_chosed = False
        employee4_chosed = True
        employee5_chosed = False
        employee6_chosed = False
        print("employee4_choose was set to: " + str(employee4_chosed))

    def employee5_choose(self):
        global employee5_chosed
        #set these all to false so only 1 at the time can be chosen
        employee1_chosed = False
        employee2_chosed = False
        employee3_chosed = False
        employee4_chosed = False
        employee5_chosed = True
        employee6_chosed = False
        print("employee5_choose was set to: " + str(employee5_chosed))

    def employee6_choose(self):
        global employee6_chosed
        #set these all to false so only 1 at the time can be chosen
        employee1_chosed = False
        employee2_chosed = False
        employee3_chosed = False
        employee4_chosed = False
        employee5_chosed = False
        employee6_chosed = True
        print("employee6_choose was set to: " + str(employee6_chosed))

    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
