from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App


class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.direction= direction
        self.goal=goal

class Screen5(Screen):
    def __init__(self, name='scr5'):
        super().__init__(name=name)
        hl = BoxLayout(orientation='horizontal')
        v1 = BoxLayout(orientation='vertical')
        v2 = BoxLayout(orientation='vertical')

        label = Label(text='Screen 5')
        btn = Button(text='Back')

        btn.on_press = self.next
        v1.add_widget(label)
        v2.add_widget(btn)
        hl.add_widget(v1)
        hl.add_widget(v2)
        self.add_widget(hl)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'scr1'
class Screen4(Screen):
    def __init__(self, name='scr4'):
        super().__init__(name=name)
        hl = BoxLayout(orientation='horizontal')
        v1 = BoxLayout(orientation='vertical')
        v2 = BoxLayout(orientation='vertical')

        label = Label(text='Screen 4')
        btn = Button(text='Back')

        btn.on_press = self.next
        v1.add_widget(label)
        v2.add_widget(btn)
        hl.add_widget(v1)
        hl.add_widget(v2)
        self.add_widget(hl)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'scr1'
class Screen3(Screen):
    def __init__(self, name='scr3'):
        super().__init__(name=name)

        hl = BoxLayout(orientation='horizontal')
        v1 = BoxLayout(orientation='vertical')
        v2 = BoxLayout(orientation='vertical')

        label = Label(text='Screen 3')
        btn = Button(text='Back')

        btn.on_press = self.next
        v1.add_widget(label)
        v2.add_widget(btn)
        hl.add_widget(v1)
        hl.add_widget(v2)
        self.add_widget(hl)

    def next(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'scr1'
class Screen2(Screen):
    def __init__(self, name='scr2'):
        super().__init__(name=name)
        hl = BoxLayout(orientation='horizontal')
        v1 = BoxLayout(orientation='vertical')
        v2 = BoxLayout(orientation='vertical')

        label = Label(text='Screen 2')
        btn = Button(text='Back', size_hint=(0.5, 0.5), pos_hint={'center_x': 1, 'top': 1})
        btn11 = Button(text='Button1', size_hint=(0.5, 0.5), pos_hint={'right': 0.5, 'bottom': 0.5})
        v1.add_widget(btn11)

        btn.on_press = self.next
        # v1.add_widget(label)
        v2.add_widget(btn)
        hl.add_widget(v1)
        hl.add_widget(v2)
        self.add_widget(hl)

    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'scr1'

class Screen1(Screen):
    def __init__(self, name='scr1', **kwargs):
        super().__init__(name=name, **kwargs)

        h1 = BoxLayout(orientation='horizontal')
        v1 = BoxLayout(orientation='vertical')
        v2 = BoxLayout(orientation='vertical')

        btn1 = Button(text='Screen 2')
        btn1.on_press = self.nextUp

        btn2 = Button(text='Screen 3')
        btn2.on_press = self.nextDown

        btn3 = Button(text='Screen 4')
        btn3.on_press = self.nextLeft

        btn4 = Button(text='Screen 5')
        btn4.on_press = self.nextRight

        label = Label(text='Screen 1')

        v1.add_widget(label)
        v2.add_widget(btn1)
        v2.add_widget(btn2)
        v2.add_widget(btn3)
        v2.add_widget(btn4)
        h1.add_widget(v1)
        h1.add_widget(v2)
        self.add_widget(h1)

    def nextUp(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'scr2'

    def nextDown(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'scr3'

    def nextLeft(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'scr4'

    def nextRight(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'scr5'
class myApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        sc = ScreenManager()
        sc.add_widget(Screen1(name='scr1'))
        sc.add_widget(Screen2(name='scr2'))
        sc.add_widget(Screen3(name='scr3'))
        sc.add_widget(Screen4(name='scr4'))
        sc.add_widget(Screen5(name='scr5'))
        return sc

app = myApp()
app.run()