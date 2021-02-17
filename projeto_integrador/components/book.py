from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('components/book.kv')


class Book(BoxLayout):
    def __init__(self, title='', authors='', link='', **kwargs):
        super().__init__(**kwargs)
        self.title_content = title
        self.authors_content = authors
        self.link_content = link
