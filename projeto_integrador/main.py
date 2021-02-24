import os
import kivy
from kivy.core.window import Window
from kivymd.app import MDApp
from screens.home import Home
from screens.downloads import Downloads
from kivy.uix.screenmanager import ScreenManager, CardTransition

__version__ = '0.0.2'

kivy.require('1.11.1')

# Window.size = (350, 580)  # Only in development


class ProjetoIntegradorApp(MDApp):
    def build(self):
        screen_manager = ScreenManager(transition=CardTransition())

        screen_manager.add_widget(Home(name='home'))
        screen_manager.add_widget(Downloads(name='downloads'))

        return screen_manager


if __name__ == '__main__':
    app = ProjetoIntegradorApp()

    if 'epub_downloads' not in os.listdir(app.user_data_dir):
        os.mkdir(app.user_data_dir + '/epub_downloads')

    app.run()
