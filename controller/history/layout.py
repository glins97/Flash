from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('view/history/layout.kv')
class HistoryLayout(ScrollView):
    def __init__(self, *args, **kwargs):
        self.history = App.get_running_app().history
        self.history.layout = self
        super(HistoryLayout, self).__init__(**kwargs)