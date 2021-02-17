import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from screens.home import Home

__version__ = '0.0.1'

kivy.require('1.11.1')

# Window.size = (350, 580)  # Only in development


class ProjetoIntegradorApp(MDApp):
    def build(self):
        return Home()


if __name__ == '__main__':
    app = ProjetoIntegradorApp()
    app.run()
