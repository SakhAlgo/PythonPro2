# напиши здесь свое приложение
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.animation import Animation

from instructions import *
from ruffier import *
from seconds import Seconds
from kivy.properties import NumericProperty

# anim = Animation(background_color=(0.73, 0.75, 0.96, 1), duration=3)

Window.clearcolor = (0, 0.5, 0.5, 0.5)
name = 'None'
age = 0
indexR = 0
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class AnimationLabel(Label):
    # nm = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # start_color = self.background_color
        start_size_h = self.size_hint
        start_pos_hint = self.pos_hint
        start_font_size = self.font_size
        # self.nm = 15

        # animate = Animation(font_size=34, duration=0.001)
        # animate = animate + Animation(pos_hint={'top': 2}, duration=0.5)
        animate = Animation(pos_hint={'top': 2}, duration=0.7)
        back = Animation(size_hint=start_size_h, pos_hint=start_pos_hint,
                         font_size=start_font_size, duration=0.7)
        self.animate = animate + back


    def start_animation(self):
        self.animate.start(self)
        self.animate.repeat = True
        # if self.nm == 15:
        #     self.animate.stop()

class InstrScreen1(Screen):
    def __init__(self, name='scr1'):
        super().__init__(name=name)
        h1 = BoxLayout(orientation='vertical')
        # h2 = BoxLayout(padding=[300,0,300,50])
        v2_1 = BoxLayout(orientation='horizontal', size_hint=(0.7, 0.08), spacing=0)
        v2_2 = BoxLayout(orientation='horizontal', size_hint=(0.7, 0.08), spacing=0)
        v2_3 = BoxLayout(orientation='horizontal', padding=50)
        v_button = BoxLayout(orientation='horizontal', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, padding=20)

        btn1 = Button(text='Начать')
        btn1.background_color = (1, 0, 0)
        # anim.start(btn1)
        btn1.on_press = self.next
        txt = '[b]'+ '[color=#4B0082]' + 'Введите имя:' + '[/color]' + '[/b]'
        labelName = Label(text=txt, markup='True')
        labelAge = Label(text='Введите возраст:')
        self.textName = TextInput(text='', multiline=False)
        self.textAge = TextInput(text='7', multiline=False)

        hintText = Label(text=txt_instruction)

        v2_3.add_widget(hintText)
        v2_1.add_widget(labelName)
        v2_1.add_widget(self.textName)
        v2_2.add_widget(labelAge)
        v2_2.add_widget(self.textAge)
        v_button.add_widget(btn1)

        h1.add_widget(v2_3)
        h1.add_widget(v2_1)
        h1.add_widget(v2_2)
        h1.add_widget(v_button)
        # h1.add_widget(h2)

        self.add_widget(h1)

    def next(self):
        global name, age

        name = self.textName.text
        age = check_int(self.textAge.text)
        if not age or age < 7:
            self.textAge.text = 'Некорректный ввод данных. '
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'scr2'


class PulseScreen2(Screen):
    def __init__(self, name='scr2'):
        super().__init__(name=name)
        self.nextScreen = False
        h1 = BoxLayout(orientation='vertical')
        v2_1 = BoxLayout(orientation='horizontal', size_hint=(0.7, 0.1), spacing=0)
        v2_3 = BoxLayout(orientation='horizontal', padding=50)
        v_button = BoxLayout(orientation='horizontal', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, padding=20)
        anime_BoxLayout = BoxLayout(size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'y': 0}, padding=20)


        self.btn1 = Button(text='Начать')
        self.btn1.on_press = self.next
        labelName = Label(text='Введите результат:')
        self.lbs_sec = Seconds(15)
        self.lbs_sec.bind(done=self.secFinished)

        self.btn2 = AnimationLabel(text='Приседай', pos_hint={'top': 1})

        self.p1 = TextInput()

        hintText = Label(text=txt_test1)


        v2_3.add_widget(hintText)
        v2_1.add_widget(labelName)
        v2_1.add_widget(self.p1)
        v_button.add_widget(self.btn1)
        anime_BoxLayout.add_widget(self.btn2)


        h1.add_widget(v2_3)
        h1.add_widget(self.lbs_sec)
        h1.add_widget(anime_BoxLayout)
        h1.add_widget(v2_1)

        h1.add_widget(v_button)

        self.add_widget(h1)
    def secFinished(self, *args):
        self.nextScreen = True
        self.btn1.set_disabled(False)
        self.p1.set_disabled(False)
        self.btn1.text = 'Продолжить'

    def next(self):
        if not self.nextScreen:
            self.btn1.set_disabled(True)
            self.p1.set_disabled(True)
            self.lbs_sec.start()
            self.btn2.start_animation()
        else:
            global p1
            self.manager.transition.direction = 'left'
            p1 = check_int(self.p1.text)
            if p1 == False or p1 < 7:
                print('Некорректный ввод данных')
                self.p1.text = 'Некорректный ввод данных'
            else:
                self.manager.current = 'scr3'


class CheckSitsScreen3(Screen):
    def __init__(self, name='scr3'):
        super().__init__(name=name)
        h1 = BoxLayout(orientation='vertical')
        v2_3 = BoxLayout(orientation='horizontal', padding=50)
        v_button = BoxLayout(orientation='horizontal', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, padding=20)

        btn1 = Button(text='Продолжить')
        btn1.on_press = self.next

        hintText = Label(text=txt_sits)
        v2_3.add_widget(hintText)
        v_button.add_widget(btn1)

        h1.add_widget(v2_3)
        h1.add_widget(v_button)

        self.add_widget(h1)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'scr4'

class Puls2Screen4(Screen):
    def __init__(self, name='scr4'):
        self.nextScreen = False
        self.tm = 0
        super().__init__(name=name)
        h1 = BoxLayout(orientation='vertical')
        # h2 = BoxLayout(padding=[300,0,300,50])
        v2_1 = BoxLayout(orientation='horizontal', size_hint=(0.7, 0.1), spacing=0)
        v2_2 = BoxLayout(orientation='horizontal', size_hint=(0.7, 0.1), spacing=0)
        v2_3 = BoxLayout(orientation='horizontal', padding=50)
        v_button = BoxLayout(orientation='horizontal', size_hint=(0.2, 0.2), pos_hint={'center_x': 0.5, 'y': 0}, padding=20)

        self.btn1 = Button(text='Начать')
        self.btn1.on_press = self.next
        labelp2 = Label(text='Результат:')
        labelp3 = Label(text='Результат после отдыха:')
        self.textp2 = TextInput()
        self.textp3 = TextInput()
        hintText = Label(text=txt_test3)

        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.secFinished)

        v2_3.add_widget(hintText)
        v2_1.add_widget(labelp2)
        v2_1.add_widget(self.textp2)
        v2_2.add_widget(labelp3)
        v2_2.add_widget(self.textp3)
        v_button.add_widget(self.btn1)

        h1.add_widget(v2_3)
        h1.add_widget(self.lbl_sec)
        h1.add_widget(v2_1)
        h1.add_widget(v2_2)
        h1.add_widget(v_button)
        # h1.add_widget(h2)

        self.add_widget(h1)
    def secFinished(self, *args):
        if self.lbl_sec.done:
            if self.tm == 0:
                self.lbl_sec.restart(30)
                self.btn1.text = 'Отдыхайте'
                self.tm = 1
            elif self.tm == 1:
                self.lbl_sec.restart(15)
                self.btn1.text = 'Считайте пульс'
                self.tm = 2
            elif self.tm == 2:
                self.nextScreen = True
                self.btn1.set_disabled(False)
                self.textp2.set_disabled(False)
                self.textp3.set_disabled(False)
                self.btn1.text = 'Завершить'

    def next(self):
        if not self.nextScreen:
            self.btn1.set_disabled(True)
            self.textp2.set_disabled(True)
            self.textp3.set_disabled(True)
            self.btn1.text = 'Считайте пульс'
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.textp2.text)
            p3 = check_int(self.textp3.text)
            if not p2 or not p3 or p2 < 0 or p3 < 0:
                self.textp2.text = 'Некорректный ввод данных'
                self.textp3.text = 'Некорректный ввод данных'
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = 'scr5'

class Screen5(Screen):
    def __init__(self, name='scr5'):
        super().__init__(name=name)
        self.h1 = BoxLayout(orientation='vertical')
        self.hintText = Label()
        self.on_enter = self.before
        self.add_widget(self.h1)

    def before(self):
        global indexR
        indexR = (4 * (p1 + p2 + p3) - 200) / 10
        self.hintText.text = name + '\n' + test(p1,p2,p3, int(age))
        self.h1.add_widget(self.hintText)

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        sc = ScreenManager()
        sc.add_widget(InstrScreen1(name='scr1'))
        sc.add_widget(PulseScreen2(name='scr2'))
        sc.add_widget(CheckSitsScreen3(name='scr3'))
        sc.add_widget(Puls2Screen4(name='scr4'))
        sc.add_widget(Screen5(name='scr5'))
        return sc

app = MyApp()
app.run()
print(name)
