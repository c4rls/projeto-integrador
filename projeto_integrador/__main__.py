from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy
kivy.require('1.11.1')


class ScreenRoot(BoxLayout):
    pass


class ProjetoIntegradorApp(App):
    def build(self):
        return ScreenRoot()


if __name__ == '__main__':
    ProjetoIntegradorApp().run()
