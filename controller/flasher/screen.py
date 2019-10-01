from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.animation import Animation

Builder.load_file('view/flasher/screen.kv')
class FlasherScreen(Screen):
    answer_label = ObjectProperty()
    question_label = ObjectProperty()

    def __init__(self, **kwargs):
        self.flasher = App.get_running_app().flasher
        self.flasher.screen = self
        super(FlasherScreen, self).__init__(**kwargs)

    def on_question_label(self, instance, obj):
        self.question_label.text = self.flasher.request_next_question()
        
    def on_answer_label(self, instance, obj):
        self.answer_label.text = self.flasher.request_answer(
            self.question_label.text)

    def update_cards(self, q, a):
        self.question_label.text = q
        self.answer_label.text = a

    def show_answer(self):
        Animation.stop_all(self.ids.answer_layout)
        Animation.stop_all(self.ids.question_layout)
        Animation(opacity=0, t='out_quad', d=0.5).start(self.ids.question_layout)
        (Animation(t='in_quad', d=0.2) + Animation(opacity=1, t='in_quad', d=1)).start(self.ids.answer_layout)

    def show_question(self):
        Animation.stop_all(self.ids.answer_layout)
        Animation.stop_all(self.ids.question_layout)
        Animation(opacity=0, t='out_quad', d=0.5).start(self.ids.answer_layout)
        (Animation(t='in_quad', d=0.2) + Animation(opacity=1, t='in_quad', d=1)).start(self.ids.question_layout)

        