from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

def getText():
    print('Test')

class Screen1(Screen):
    def __init__(self, name='scr1'):
        super().__init__(name=name)
        btn = Button(text='Switch to a second screen')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'scr2'

class Screen2(Screen):
    def __init__(self, name='scr2'):
        super().__init__(name=name)
        btn = Button(text='Switch to a first screen')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'scr1'

class myApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1())
        sm.add_widget(Screen2())
        return  sm
        # h1 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        # label1 = Label(text='123', color=(1,0,0))
        # box = BoxLayout(orientation='vertical', padding=8, spacing=8)
        # btn1 = Button(text='Button')
        # btn1.on_press = getText
        # h1.add_widget(label1)
        # h1.add_widget(box)
        # h1.add_widget(btn1)
        # return h1

app = myApp()
app.run()