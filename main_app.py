from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

age = 7
name = ""
p1, p2, p3 = 0, 0, 0

#Клас для першого вікна (вікна з інтсрукціями до програми)
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        instr = Label(text = txt_instruction)
        lbl1 = Label(text="Введіть ім'я:", halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Введіть вік:', halign='right')
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Почати', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    #функція, яка спрацьовуватиме при натисканні на кнопку "Продовжити" на першому екрані
    def next(self):
        #в глобальні змінні name та age записуємо ім'я та вік, які користувач записав в наші TextInput-и
        global name, age
        name = self.in_name.text
        age = int(self.in_age.text)
        #міняємо поточний екран на екран під назвою "pulse1" (тобто другий екран)
        self.manager.current = 'pulse1'



#КЛас для другого вікна (тут треба вписати результат першого вимірювання пульсу)
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text = txt_test1)    
        lbl_result = Label(text='Введіть результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)

        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        self.btn = Button(text='Продовжити', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    #функція, яка спрацьовуватиме при натисканні на кнопку "Продовжити" на другому екрані
    def next(self):
        #в глобальну змінну p1 записуємо результат вимірювання пульсу, який користувач записав в наш TextInput
        global p1
        p1 = int(self.in_result.text)
        #міняємо поточний екран на екран під назвою "sits" (тобто третій екран)
        self.manager.current = 'sits'



#Клас для третього вікна (тут людині показується фраза про те, що їй треба зробити 30 присідань)
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #1) створити Label, якому в параметр text встановити значення змінної txt_sits (інструкція для присідань)

        #2) створити кнопку "Продовжити" і підключити до неї метод next (можна просто скопіювати з попереднього класу)
        
        #3) Створити вертикальний лейаут (в ньому padding та spacing мають дорівнювати 8)

        #4) Додати на створений вертикальний лейаут віджет з інструкцією для присідань(створений в першому пункті)

        #5) Додати на створений вертикальний лейаут кнопку(створену в другому пункті)

        #6) Додати цей вертикальний лейаут у вікно (у self)


    #функція, яка спрацьовуватиме при натисканні на кнопку "Продовжити" на третьому екрані
    def next(self):
       self.manager.current = 'pulse2'



#Клас для четвертого вікна (тут людині треба вписати свій пульс одразу після присідань та після 30-секундної перерви)
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_test3)
        lbl_result1 = Label(text='Результат:', halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)
      
        lbl_result2 = Label(text='Результат після відпочинку:', halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)

        self.btn = Button(text='Завершити', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    #функція, яка спрацьовуватиме при натисканні на кнопку "Продовжити" на четвертому екрані
    def next(self):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = 'result'


#Клас для п'ятого вікна (тут буде показаний результат)
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.instr = Label(text = name + '\n' + test(p1, p2, p3, age))

        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)



#Клас, який визначає наш мобільний додаток
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm
    

app = HeartCheck()
app.run()
