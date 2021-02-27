from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel, MDIcon
from kivy.properties import NumericProperty

Builder.load_file('screens/ebook_viewer.kv')


class EBookViewer(Screen):
    current_page = NumericProperty(1)
    max_page = NumericProperty(10)

    def set_book(self, book):
        pass

    def set_previous_screen(self, previous_screen):
        self.previous_screen = previous_screen

    def go_to_previous_screen(self):
        app = App.get_running_app()

        app.root.current = self.previous_screen

    def go_to_next_page(self):
        self.current_page = self.current_page if self.current_page == self.max_page else self.current_page + 1

    def go_to_previous_page(self):
        self.current_page = 1 if self.current_page == 1 else self.current_page - 1
