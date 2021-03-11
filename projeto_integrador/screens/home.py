from threading import Thread, Event
from kivy.lang import Builder
from kivy.clock import mainthread
from gutendex import search_books
from components.book_card import BookCard
from components.top_bar import TopBar
from components.side_menu import SideMenu
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivy.uix.modalview import ModalView
from kivymd.uix.spinner import MDSpinner


Builder.load_file('screens/home.kv')


class Home(Screen):
    modal_spinner: ModalView = None

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self._stop_event = Event()

    def stop(self):
        self._stop_event.set()

    def _get_books(self):
        search_box = self.ids.search_box
        books_list = self.ids.books_list

        terms = search_box.ids.input.text.strip()
        if not terms:
            search_box.ids.input.text = ''
            return

        modal_spinner = ModalView(size_hint=(None, None), size=(
            100, 100), auto_dismiss=False, background='', background_color=(1, 1, 1, 0))
        modal_spinner.add_widget(MDSpinner(size_hint=(0.7, 0.7), active=True))
        self.modal_spinner = modal_spinner

        def thread_func():
            books = search_books(terms)
            self._update_books(books)

        modal_spinner.open()

        Thread(target=thread_func).start()

    @mainthread
    def _update_books(self, books):
        search_box = self.ids.search_box
        books_list = self.ids.books_list

        books_list.ids.container.clear_widgets()

        for book in books:
            book_widget = BookCard(
                book=book,
                download_button_func=self._download_book,
                remove_button_func=self._remove_book)
            books_list.ids.container.add_widget(book_widget)

        search_box.ids.input.text = ''
        books_list.ids.found_books.text = str(len(
            books)) + ' livro(s) encontrado(s)' if len(books) > 0 else 'Nenhum livro encontrado'

        self.modal_spinner.dismiss()

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
