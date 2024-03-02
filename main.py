from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


#Клас, який визначає кнопки, що переключатимуть екрани
class ScrButton(Button):
    def __init__(self, screen, direction='right', goal="main", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


#Клас, який визначає основний екран
class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding = 8, spacing = 8)
        vl.add_widget(ScrButton(self, direction="down", goal="first", text="1"))
        vl.add_widget(ScrButton(self, direction="left", goal="second", text="2"))
        vl.add_widget(ScrButton(self, direction="up", goal="third", text="3"))
        vl.add_widget(ScrButton(self, direction="right", goal="fourth", text="4"))
        txt = Label(text="Вибери екран")
        hl = BoxLayout()
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)


#Клас, який визначає перший екран
class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical')
        self.txt = Label(text= 'Екран: 1')
        vl.add_widget(self.txt)  

        #size_hint - частка, яку займатиме цей лейаут по осі Х(80%) та Y(10%) відносно того, де він знаходиться
        hl_0 = BoxLayout(size_hint=(0.8, 0.1))
        lbl1 = Label(text='Введіть пароль:', halign='right')
        self.input = TextInput(multiline=False)  

        hl_0.add_widget(lbl1)
        hl_0.add_widget(self.input)
        vl.add_widget(hl_0)

        #pos_hint - змінює положення віджету. pos_hint={<яка_частина_віджета>: <де_розташована_на_екрані>}
        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        btn_false = Button(text="OK!")
        btn_back = ScrButton(self, direction='right', goal='main', text="Назад") 

        hl.add_widget(btn_false)
        hl.add_widget(btn_back)
        vl.add_widget(hl)
        self.add_widget(vl)
        btn_false.on_press = self.change_text

    def change_text(self):
        self.txt.text = self.input.text + '? Не спрацювало ...'


#Клас, який визначає другий екран
# ЗАВДАННЯ: створити вертикальний лейаут і закріпити на нього:
#1. Поле для введення тексту
#2. Горизонтальний лейаут з двома кнопками: 
#   - "Назад", яка повертатиме користувача на основний екран
#   - "Очистити", яка буде чистити поле для введення тексту. Для цього запрограмувати метод clear_text(self)
class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn_back = ScrButton(self, direction='up', goal='main', text="Назад")
        self.add_widget(btn_back)


#Клас, який визначає третій екран
# ЗАВДАННЯ: запрограмувати екран самостійно, як завгодно
class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn_back = ScrButton(self, direction='up', goal='main', text="Назад")
        self.add_widget(btn_back)


#Клас, який визначає четвертий екран
# ЗАВДАННЯ: запрограмувати екран самостійно, як завгодно
class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn_back = ScrButton(self, direction='up', goal='main', text="Назад")
        self.add_widget(btn_back)


#Клас, який визначає наш мобільний додаток
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm

app = MyApp()
app.run()
