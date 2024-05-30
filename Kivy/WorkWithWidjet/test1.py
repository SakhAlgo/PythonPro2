from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        h1 = BoxLayout()
        # h2 = BoxLayout(orientation='horizontal')
        h3 = BoxLayout(orientation='horizontal', padding=200)

        btn1 = Button(text='Button1', size_hint=(0.5, 0.5), pos_hint={'center_x': 1, 'top': 1})
        btn2 = Button(text='Button2', size_hint=(0.5, 0.5), pos_hint={'right': 0.5, 'bottom': 0.5})
        label = Label(text='Label')

        # h2.add_widget(label)
        h3.add_widget(btn1)
        h3.add_widget(btn2)
        # h1.add_widget(h2)
        h1.add_widget(h3)


        return h1


app = MyApp()
app.run()