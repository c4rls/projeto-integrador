from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.theming import ThemableBehavior


Builder.load_file('components/side_menu.kv')


class SideMenu(MDNavigationDrawer):
    def goToScreen(self, screen_name):
        app = App.get_running_app()

        if screen_name == 'downloads':
            app.root.get_screen('downloads').load_books()

        app.root.current = screen_name
        app.root.current_screen.ids.side_menu.set_state('closed')
