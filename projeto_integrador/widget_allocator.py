from threading import Event, Thread
from kivy.clock import Clock


class WidgetAllocator:
    '''A class to manage the creation of widgets more efficiently.

    This management is done through a thread working in the background,
    which automatically creates the widgets as soon as the number of them
    is below the limit.
    '''

    def __init__(self, config=None):
        '''*config* must be a list of tuples in the following format:
        (name: str, widget_class: Widget Class, lower_limit: int, upper_limit: int)
        '''

        self._config = config
        self._allocated_widgets = []
        self._virtual_widgets = []
        self._stop = Event()
        self._thread = None

        self._reset_widgets()

    def _reset_widgets(self):
        self._allocated_widgets = []
        self._virtual_widgets = []

        for i in self._config:
            if i[2] >= i[3]:
                raise Exception()

            self._allocated_widgets.append([])
            self._virtual_widgets.append(0)

    def _type_to_index(self, type_widget):
        for index, i in enumerate(self._config):
            if i[0] == type_widget:
                return index

        raise Exception()

    def get_widget(self, type_widget):
        index = self._type_to_index(type_widget)

        if self._allocated_widgets[index]:
            self._virtual_widgets[index] -= 1
            return self._allocated_widgets[index].pop()

        return self._create_widget(type_widget)

    def _create_widget(self, type_widget):
        for i in self._config:
            if i[0] == type_widget:
                return i[1]()

        raise Exception()

    def _allocate_widgets(self, type_widget, amount):
        index = self._type_to_index(type_widget)

        for _ in range(0, amount):
            if self._stop.is_set():
                return

            widget = self._create_widget(type_widget)

            self._allocated_widgets[index].append(widget)

    def _request_allocation(self, type_widget, amount):
        Clock.schedule_once(
            lambda _: self._allocate_widgets(type_widget, amount), 0)

    def start_allocation(self):
        if self._thread:
            raise Exception()

        def thread_func():
            while True:
                if self._stop.is_set():
                    break

                for index, i in enumerate(self._config):
                    if self._virtual_widgets[index] < i[2]:
                        amount_widgets = i[3] - self._virtual_widgets[index]
                        self._virtual_widgets[index] = i[3]
                        self._request_allocation(i[0], amount_widgets)

            self._thread = None

        thread = Thread(target=thread_func)
        self._thread = thread
        self._stop.clear()

        thread.start()

    def stop_allocation(self):
        self._stop.set()

    def clear_allocated_widgets(self):
        self._reset_widgets()

    def allocation_is_active(self):
        return bool(self._thread)
