from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty

Builder.load_file('view/history/selector.kv')
class HistorySelector(Button):
    question = StringProperty('')
    answer = StringProperty('')
    status = StringProperty('')
    
    def __init__(self, *args, **kwargs):
        super(HistorySelector, self).__init__(**kwargs)