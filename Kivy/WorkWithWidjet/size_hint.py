# button = Button(
#    text='Hello world',
#    size_hint=(.5, .25))

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        h1 = BoxLayout(orientation='horizontal')
        btn1 = Button(text='Button1', pos_hint={'center_y':1})


        h1.add_widget(btn1)


        return h1


app = MyApp()
app.run()