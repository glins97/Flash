from .selector import HistorySelector

class HistoryManager(object):
    def __init__(self, *args, **kwargs):
        self.layout = None
        self.app = None
        self.currently_displaying = False

    def keyboard_hook(self, window, key, *largs):
        supported_keys = [
            273, 274, 275
        ]

        if key not in supported_keys:
            return

        if self.currently_displaying: 
            self.currently_displaying = False
            return # avoid selector duplicate

        status = 'w'
        if key == 274:
            status = 'r'
        elif key == 273:
            status = 'g'

        flasher = self.app.flasher
        question_index = flasher.current_question_index
        question = flasher.questions_listed[question_index]
        answer = flasher.request_answer(question)
        b = HistorySelector(
            question=question,
            answer=answer,
            status=status,
            size_hint=(None, 1), 
            width=self.layout.width * 0.1 - 
                self.layout.ids.grid_layout.spacing[0])
        self.layout.ids.grid_layout.add_widget(b)
        self.layout.scroll_to(b)