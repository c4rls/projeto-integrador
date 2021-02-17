from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('components/side_menu.kv')


class SideMenu(MDNavigationDrawer):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass
