from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        h1 = BoxLayout(orientation='vertical')
        # h2 = BoxLayout(orientation='horizontal')
        h3 = BoxLayout(orientation='horizontal', padding=200)

        btn1 = Button(text='Button1', size_hint=(None, None), width=500, height=100)
        btn2 = Button(text='Button1', size_hint=(None, None), width=100, height=100)

        h1.add_widget(btn2)
        h1.add_widget(btn1)
        return h1


app = MyApp()
app.run()