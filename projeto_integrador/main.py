import os
import kivy
from kivy.core.window import Window
from kivymd.app import MDApp
from screens.home import Home
from screens.downloads import Downloads
from screens.ebook_viewer import EBookViewer
from kivy.uix.screenmanager import ScreenManager, CardTransition

__version__ = '0.0.3'

kivy.require('1.11.1')

# Window.size = (350, 580)  # Only in development


class ProjetoIntegradorApp(MDApp):
    def on_stop(self):
        self._stop_jobs()

    def _stop_jobs(self):
        self.root.get_screen('home').stop()
        self.root.get_screen('downloads').stop()
        self.root.get_screen('ebook_viewer').stop()

    def build(self):
        screen_manager = ScreenManager(transition=CardTransition())

        screen_manager.add_widget(Home(name='home'))
        screen_manager.add_widget(Downloads(name='downloads'))
        screen_manager.add_widget(EBookViewer(name='ebook_viewer'))

        return screen_manager


if __name__ == '__main__':
    app = ProjetoIntegradorApp()

    if 'epub_downloads' not in os.listdir(app.user_data_dir):
        os.mkdir(app.user_data_dir + '/epub_downloads')

    app.run()
