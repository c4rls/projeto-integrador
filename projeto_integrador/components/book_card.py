from kivy.app import App
from kivy.lang import Builder
from kivy.clock import mainthread
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file('components/book_card.kv')


class BookCard(MDCard):
    title_content = StringProperty('')

    def __init__(self,
                 book=None,
                 download_button_func=None,
                 remove_button_func=None,
                 **kwargs):

        super(BookCard, self).__init__(**kwargs)
        self.title_content = book.title
        self.book = book
        self.is_opened = False
        self.download_button_func = download_button_func
        self.remove_button_func = remove_button_func

    def open_or_close_card(self):
        if self.is_opened:
            self.ids.content.clear_widgets()
            self.is_opened = False
            return

        self.is_opened = True
        card_content = BookCardContent()

        epub_is_avaliable = self.book.epub_is_avaliable()
        epub_is_downloaded = self.book.epub_is_downloaded()

        card_content.ids.authors.text = 'Autores: ' + \
            ' - '.join([x.name for x in self.book.authors])
        card_content.ids.epub_download.text = 'Download em ePUB: ' + \
            'Sim' if epub_is_avaliable else 'Não'

        card_content.ids.read_button.disabled = True if not epub_is_downloaded else False
        card_content.ids.read_button.on_release = self.read_book

        card_content.ids.download_button.disabled = True if not epub_is_avaliable else epub_is_downloaded
        card_content.ids.download_button.on_release = self.download_book

        card_content.ids.remove_button.disabled = True if not epub_is_avaliable else not epub_is_downloaded
        card_content.ids.remove_button.on_release = self.remove_book

        self.ids.content.add_widget(card_content)

    def read_book(self):
        app = App.get_running_app()

        ebook_viewer = app.root.get_screen('ebook_viewer')
        ebook_viewer.set_book(self.book)
        ebook_viewer.set_previous_screen(app.root.current)
        ebook_viewer.get_pages()
        ebook_viewer.show_page(0)

        app.root.current = 'ebook_viewer'

    def download_book(self):
        @mainthread
        def func():
            card_content = self.ids.content.children[0]

            card_content.ids.read_button.disabled = False
            card_content.ids.download_button.disabled = True
            card_content.ids.remove_button.disabled = False

        self.download_button_func(book=self.book, func=func)

    def remove_book(self):
        @mainthread
        def func():
            card_content = self.ids.content.children[0]

            card_content.ids.read_button.disabled = True
            card_content.ids.download_button.disabled = False
            card_content.ids.remove_button.disabled = True

        self.remove_button_func(book=self.book, func=func)


class BookCardContent(BoxLayout):
    def __init__(self, **kwargs):
        super(BookCardContent, self).__init__(**kwargs)
