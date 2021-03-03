from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from typography import Title, Paragraph, Page, TypographyList
from ebooklib.epub import read_epub
from utils import get_links_from_toc, get_page_content, parse_content

Builder.load_file('screens/ebook_viewer.kv')


class EBookViewer(Screen):
    current_page = NumericProperty(1)
    max_page = NumericProperty(1)

    def __init__(self, **kwargs):
        super(EBookViewer, self).__init__(**kwargs)
        self.previous_screen = ''
        self.pages = []

    def set_book(self, book):
        self.book = book
        self.get_pages()
        self.render_page(0)

    def get_pages(self):
        self.pages = []

        app = App.get_running_app()

        book_file = read_epub(app.user_data_dir +
                              '/epub_downloads/' + self.book.id + '.epub')
        links = get_links_from_toc(book_file.toc)

        for index, link in enumerate(links):
            file_name, start_identifier = link.href.split('#')

            next_file_name, end_identifier = links[index + 1].href.split(
                '#') if index + 1 < len(links) else [None, None]

            content = book_file.get_item_with_href(file_name).get_content()
            page_content = None

            if next_file_name == file_name:
                page_content = get_page_content(
                    content, start_identifier, end_identifier)
            else:
                page_content = get_page_content(
                    content, start_identifier, None)

            parsed_content = parse_content(page_content)

            page = Page(parsed_content)
            self.pages.append(page)

        self.current_page = 1
        self.max_page = len(self.pages)

    def render_page(self, index):
        container = self.ids.container
        container.clear_widgets()

        page = EBookViewerPage(page=self.pages[index])
        page.render()

        container.add_widget(page)

    def set_previous_screen(self, previous_screen):
        self.previous_screen = previous_screen

    def go_to_previous_screen(self):
        app = App.get_running_app()

        app.root.current = self.previous_screen if self.previous_screen else 'home'

    def go_to_next_page(self):
        self.current_page = self.current_page if self.current_page == self.max_page else self.current_page + 1
        self.render_page(self.current_page - 1)

    def go_to_previous_page(self):
        self.current_page = 1 if self.current_page == 1 else self.current_page - 1
        self.render_page(self.current_page - 1)


class EBookViewerPage(BoxLayout):
    def __init__(self, page: Page = None, **kwargs):
        super(EBookViewerPage, self).__init__(**kwargs)
        self.page = page
        self.widgets = []

    def render(self):
        self.widgets.clear()
        self.ids.container.clear_widgets()

        if not self.page:
            return

        for i in self.page.content.text_list:
            if isinstance(i, Title):
                self.widgets.append(EBookViewerTitle(text=i.text))
                self.widgets.append(EBookViewerSeparator(multiplier=2))
            elif isinstance(i, Paragraph):
                self.widgets.append(EBookViewerParagraph(text=i.text))
                self.widgets.append(EBookViewerSeparator())

        for widget in self.widgets:
            self.ids.container.add_widget(widget)


class EBookViewerTitle(MDLabel):
    def __init__(self, text='', **kwargs):
        super(EBookViewerTitle, self).__init__(**kwargs)
        self.text = text


class EBookViewerParagraph(MDLabel):
    def __init__(self, text='', **kwargs):
        super(EBookViewerParagraph, self).__init__(**kwargs)
        self.text = text


class EBookViewerSeparator(Widget):
    multiplier = NumericProperty(1)

    def __init__(self, multiplier=1, **kwargs):
        super(EBookViewerSeparator, self).__init__(**kwargs)
        self.multiplier = multiplier
