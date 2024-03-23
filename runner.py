from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout

class Runner(BoxLayout):
    value = NumericProperty(0)              # скільки зроблено переміщень
    finished = BooleanProperty(False)       # чи зроблені всі переміщення

    def __init__(self, total,  steptime, autorepeat=True,
                bcolor=(0.73, 0.15, 0.96, 1),
                btext_inprogress='Присідання',
                **kwargs):

        super().__init__(**kwargs)

        self.total = total
        self.autorepeat = autorepeat
        self.btext_inprogress = btext_inprogress
        #анімація складається здвох частин: спочатку позиція має поміняютися на 'top': 0.1, а потім знову помінятися на top': 1.0. Все це сумарно за 1.5 секунди
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2) + Animation(pos_hint={'top': 1.0}, duration=steptime/2))
        #під час анімації виконуватиметься метод next
        self.animation.on_progress = self.next
        #створюємо кнопку, яка і є нашим бігунком
        self.btn = Button(size_hint=(1, 0.1), pos_hint={'top': 1.0}, background_color=bcolor)
        self.add_widget(self.btn)


    #метод, який запускає бігунок
    def start(self):
        self.value = 0
        self.finished = False
        self.btn.text = self.btext_inprogress 
        #запускаємо автоповтор анімації
        if self.autorepeat:
            self.animation.repeat = True
        #включаємо анімацію для self.btn 
        self.animation.start(self.btn)


    #метод, який спрацьовує під час анімаії
    def next(self, widget, step):
        #збільшуємо кількість переміщень на 1
        if step == 1.0:
            self.value += 1
            #якщо зроблено достатньо переміщень
            if self.value >= self.total:
                #зупиняємо автоповтор анімації
                self.animation.repeat = False
                self.finished = True
