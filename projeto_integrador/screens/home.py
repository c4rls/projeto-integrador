from gutendex import search_books
from kivy.lang import Builder
from components.book import Book
from components.top_bar import TopBar
from components.side_menu import SideMenu
from kivymd.uix.screen import Screen


Builder.load_file('screens/home.kv')


class Home(Screen):
    def getBooks(self):
        terms = self.search_box.ids.search_input.text.strip()
        if not terms:
            return

        self.books_list.ids.books_list.clear_widgets()
        books = search_books(terms)

        for book in books:
            authors = ' - '.join([x.name for x in book.authors])
            link = book.formats['application/epub+zip'] if book.epub_is_avaliable(
            ) else 'Não disponível'

            book_widget = Book(title=book.title, authors=authors, link=link)
            self.books_list.ids.books_list.add_widget(book_widget)

        self.search_box.ids.search_input.text = ''
        self.books_list.ids.books_header.found_books = len(books)
