import math

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '250')
Config.set('graphics', 'resizable', 0)

with open("quad_eq.kv", encoding='utf8') as f:
    Builder.load_string(f.read())


class RootWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

    def solve(self):
        a = float(self.ids.a.text)
        b = float(self.ids.b.text)
        c = float(self.ids.c.text)
        discriminant = b ** 2 - 4*a*c
        if discriminant > 0:
            sqrt_discriminant = math.sqrt(discriminant)
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
            self.ids.d.text = 'D = ' + str(discriminant)
            if x1 < x2:
                self.ids.x.text = 'x1 = %.2f \nx2 = %.2f' % (x1, x2)
            else:
                self.ids.x.text = 'x1 = %.2f \nx2 = %.2f' % (x2, x1)
        elif discriminant == 0:
            x = (-b) / (2*a)
            self.ids.d.text = 'D = 0'
            self.ids.x.text = 'x1 = %.2f' % (x)
        else:
            self.ids.d.text = 'D < 0'
            self.ids.x.text = 'Нет корней'
        # self.ids.but_n.text = name


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()


    # белый цвет фона
    # canvas.before:
    #     Color:
    #         rgba: 1, 1, 1, 1
    #     Rectangle:
    #         pos: self.pos
    #         size: self.size
