from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from typography import Title, Paragraph, Page, TypographyList

Builder.load_file('screens/ebook_viewer.kv')

content = TypographyList([
    Title(text='Obito do autor'),
    Paragraph(text='Algum tempo hesitei se devia abrir estas memorias pelo principio ou pelo fim, isto é, se poria em primeiro logar o meu nascimento ou a minha morte. Supposto o uso vulgar seja começar pelo nascimento, duas considerações me levaram a adoptar differente methodo: a primeira é que eu não sou propriamente um autor defunto, mas um defunto autor, para quem a campa foi outro berço; a segunda é que o escripto ficaria assim mais galante e mais novo. Moysés, que tambem contou a sua morte, não a poz no introito, mas no cabo: differença radical entre este livro e o Pentateuco.'),
    Paragraph(text='Dito isto, expirei ás duas horas da tarde de uma sexta feira do mez de agosto de 1869, na minha bella chacara de Catumby. Tinha uns sessenta e quatro annos, rijos e prosperos, era solteiro, possuia cerca de tresentos contos e fui acompanhado ao cemiterio por onze amigos. Onze amigos! Verdade é que não houve cartas nem annuncios. Accresce que chovia—peneirava—uma chuvinha miuda, triste e constante, tão constante e tão triste, que levou um daquelles fieis da ultima hora a intercalar esta engenhosa idéa no discurso que proferiu á beira de minha cova:—«Vós, que o conhecestes, meus senhores, vós podeis dizer commigo que a natureza parece estar chorando a perda irreparavel de um dos mais bellos caracteres que tem honrado a humanidade. Este ar sombrio, estas gotas do ceu, aquellas nuvens escuras que cobrem o azul como um crepe funereo, tudo isso é a dor crua e má que lhe róe á natureza as mais intimas entranhas; tudo isso é um sublime louvor ao nosso illustre finado.»'),
    Paragraph(text='Bom e fiel amigo! Não, não me arrependo das vinte apolices que lhe deixei. E foi assim que cheguei á clausula dos meus dias; foi assim que me encaminhei para o undiscovered country de Hamlet, sem as ancias nem as duvidas do moço principe, mas pausado e tropego, como quem se retira tarde do expectaculo. Tarde e aborrecido. Viram-me ir umas nove ou dez pessoas, entre ellas tres senhoras,—minha irmã Sabina, casada com o Cotrim,—a filha, um lyrio do valle,—e... Tenham paciencia! daqui a pouco lhes direi quem era a terceira senhora. Contentem-se de saber que essa anonyma, ainda que não parenta, padeceu mais do que as parentas. É verdade, padeceu mais. Não digo que se carpisse, não digo que se deixasse rolar pelo chão, epileptica. Nem o meu obito era cousa altamente dramatica... Um solteirão que expira aos sessenta e quatro annos, não parece que reuna em si todos os elementos de uma tragedia. E dado que sim, o que menos convinha a essa anonyma era apparental-o. De pé, á cabeceira da cama, com os olhos estúpidos, a boca entreaberta, a triste senhora mal podia crêr na minha extincção.'),
    Paragraph(text='Mais uma prova do carater generozo e bizarro do selvajem brazileiro. Lonje de torturarem seu prizioneiro, ao contrario se esforçavam em alegrar-lhes os ultimos dias pelo amor; davam-lhe uma espoza; e tão grande honra era esta que o vencedor a rezervava para sua filha ou irmã virjem; e se não a tinha, para a filha de algum dos principais da taba.'),
    Paragraph(text='Ora, cunhãmembira significa saído do ventre da mulher. A lingua tupí não tinha outro modo de dezignar a maternidade: taíra—isto é, saído do sangue, diziam do filho ácerca do pai; e membira, diziam do filho ácerca da mãi. Na expressão cunhãmembira não ha senão a antepozição do substantivo cunham (mulher) que os indios suprimiam por superfluo; assim como suprimiam na outra palavra dizendo simplesmente taíra e não aba-taíra saído do sangue do varão.'),
    Paragraph(text='Jussara.—«Nas povoações feitas em terra têm muitas nações guerreiras a providencia de as segurarem e munirem com fortes muralhas, não de pedra, mas de estacas do páu duro como pedra. Outros as fabricam de palmeira, que chamam jussara, cujos espinhos são tão grandes e duros, que servem a muitos de agulhas de fazer meias; e as trincheiras feitas de jussara são mais seguras que as mais bem reguladas fortalezas; porque de modo nenhum se podem penetrar e romper senão com fogo por crecerem não só cheias de grandes estrepes ou agudos espinhos, mas tão enlaçadas e enleadas umas com outras que se fazem impenetraveis. (Tezouro descoberto no rio Amazonas, Part. 2a, cap. 1o, no 2o vol. da Rev. do Instituto, paj. 350.)'),
])


class EBookViewer(Screen):
    current_page = NumericProperty(1)
    max_page = NumericProperty(1)

    def __init__(self, **kwargs):
        super(EBookViewer, self).__init__(**kwargs)
        self.previous_screen = ''
        self.set_book(None)

    def set_book(self, book):
        self.book = book
        self.get_pages()
        self.render_page(0)

    def get_pages(self):
        self.pages = [Page(content.get_chunk(start=0, end=3)),
                      Page(content.get_chunk(start=4, end=6))]

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
