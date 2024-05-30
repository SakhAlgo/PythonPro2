# в программе описан класс MyInput - это TextInput, который хранит
# свойство mytext. При изменении текста это свойство тоже меняется
# (это перевернутый текст, но снаружи виджета мы не обязаны знать алгоритм).
# Далее создаётся интерфейс, в котором обрабатывается изменение свойства mytext:
# каждый раз при изменении это свойство отображается на label
# см. строки 15, 21, 28, 33

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty


class MyInput(TextInput):
    # mytext = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.bind(text=self.changevalue)

    # def changevalue(self, *args):
    #     self.mytext = self.text


class MyApp(App):
    def build(self):
        mainBox = BoxLayout(orientation='vertical', padding=20)
        self.l1 = MyInput()
        self.l1.bind(text=self.textchanged)
        self.l2 = Label()
        mainBox.add_widget(self.l1)
        mainBox.add_widget(self.l2)
        return mainBox

    def textchanged(self, *args):
        self.l2.text = self.l1.text


app = MyApp()
app.run()
