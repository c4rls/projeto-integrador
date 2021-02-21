import os
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from components.top_bar import TopBar
from components.side_menu import SideMenu
from kivymd.uix.label import MDLabel
from components.book_card import BookCard
from gutendex import get_books_by_ids

Builder.load_file('screens/downloads.kv')


class Downloads(Screen):
    def __init__(self, **kwargs):
        super(Downloads, self).__init__(**kwargs)
        self.load_books()

    def load_books(self):
        self.ids.books_list.clear_widgets()

        files = os.listdir(
            App.get_running_app().user_data_dir + '/epub_downloads')
        books_ids = list(map(lambda x: x.split('.epub')[0], files))

        if len(books_ids) > 0:
            books = get_books_by_ids(books_ids)

            for book in books:
                book_widget = BookCard(book=book)
                self.ids.books_list.add_widget(book_widget)
