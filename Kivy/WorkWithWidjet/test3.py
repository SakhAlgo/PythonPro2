from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        h1 = BoxLayout(orientation='vertical', padding=200)

        btn1 = Button(text='Button1', size_hint=(1, 1), pos_hint={'cener_x': 1, 'center_y': 1})
        btn2 = Button(text='Button2', size_hint=(None, 1), pos_hint={'cener_x': 1, 'center_y': 1}, width='55sp')
        h1.add_widget(btn1)
        h1.add_widget(btn2)

        return h1


app = MyApp()
app.run()