from gutendex import search_books
from kivy.lang import Builder
from components.book_card import BookCard
from components.top_bar import TopBar
from components.side_menu import SideMenu
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton


Builder.load_file('screens/home.kv')


class Home(Screen):
    def getBooks(self):
        search_box = self.ids.search_box
        books_list = self.ids.books_list

        terms = search_box.ids.input.text.strip()
        if not terms:
            search_box.ids.input.text = ''
            return

        books = search_books(terms)
        books_list.ids.container.clear_widgets()

        for book in books:
            book_widget = BookCard(book=book)
            books_list.ids.container.add_widget(book_widget)

        search_box.ids.input.text = ''
        books_list.ids.found_books.text = str(len(
            books)) + ' livros encontrados' if len(books) > 0 else 'Nenhum livro encontrado'
