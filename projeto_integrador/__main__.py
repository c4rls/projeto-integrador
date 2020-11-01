from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('1.11.1')


class ProjetoIntegradorApp(App):
    def build(self):
        return Label(text='Projeto Integrador')


if __name__ == '__main__':
    ProjetoIntegradorApp().run()
