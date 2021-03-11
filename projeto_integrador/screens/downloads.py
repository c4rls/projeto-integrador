import os
from threading import Thread, Event
from kivy.app import App
from kivy.lang import Builder
from gutendex import get_books_by_ids
from kivy.clock import mainthread
from kivymd.uix.screen import Screen
from components.top_bar import TopBar
from components.side_menu import SideMenu
from kivymd.uix.label import MDLabel
from components.book_card import BookCard
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner

Builder.load_file('screens/downloads.kv')


class Downloads(Screen):
    def __init__(self, **kwargs):
        super(Downloads, self).__init__(**kwargs)
        self.load_books()
        self._stop_event = Event()

    def stop(self):
        self._stop_event.set()

    def load_books(self):
        self.ids.books_list.clear_widgets()

        def thread_func():
            files = os.listdir(
                App.get_running_app().user_data_dir + '/epub_downloads')
            books_ids = list(map(lambda x: x.split('.epub')[0], files))

            books = []
            if len(books_ids) > 0:
                books = get_books_by_ids(books_ids)

            self._update_books(books)

        Thread(target=thread_func).start()

    @mainthread
    def _update_books(self, books):
        self.ids.books_list.clear_widgets()

        for book in books:
            book_widget = BookCard(
                book=book,
                download_button_func=self._download_book,
                remove_button_func=self._remove_book)
            self.ids.books_list.add_widget(book_widget)

    def _download_book(self, book=None, func=None):
        modal_spinner = ModalView(size_hint=(None, None), size=(
            100, 100), auto_dismiss=False, background='', background_color=(1, 1, 1, 0))
        modal_spinner.add_widget(MDSpinner(size_hint=(0.7, 0.7), active=True))
        self.modal_spinner = modal_spinner

        modal_spinner.open()

        def thread_func():
            book.epub_download()
            clean_func()

        @mainthread
        def clean_func():
            func()
            modal_spinner.dismiss()

        Thread(target=thread_func).start()

    def _remove_book(self, book=None, func=None):
        modal_spinner = ModalView(size_hint=(None, None), size=(
            100, 100), auto_dismiss=False, background='', background_color=(1, 1, 1, 0))
        modal_spinner.add_widget(MDSpinner(size_hint=(0.7, 0.7), active=True))
        self.modal_spinner = modal_spinner

        modal_spinner.open()

        def thread_func():
            book.epub_remove()
            clear_func()

        @mainthread
        def clear_func():
            func()
            modal_spinner.dismiss()

        Thread(target=thread_func).start()
