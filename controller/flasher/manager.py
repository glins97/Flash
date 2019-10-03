from random import randint

class FlasherManager(object):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename
        self.questions = {}
        self.questions_listed = []
        self.current_question_index = -1
        self.state = 'q'
        self.screen = None
        self.load()
    
    def toggle_card_view(self):
        if self.state == 'q':
            self.state = 'a'
            self.screen.show_answer();            

        elif self.state == 'a':
            self.state = 'q'
            self.screen.show_question();            

    def show_next_card(self):
        q = self.request_next_question()
        a = self.request_answer(q)
        self.screen.update_cards(q, a)
        self.screen.show_question();     

    def request_next_question(self):
        self.current_question_index += 1
        return self.questions_listed[self.current_question_index]

    def request_answer(self, question):
        return self.questions[question]['answer']

    def keyboard_hook(self, window, key, *largs):
        if key == 13 or key == 271: # enter
            self.toggle_card_view()

        if key in [273, 274, 275]:
            self.show_next_card()
            
    def load(self):
        self.questions = {}
        src = ''

        with open(self.filename) as f:
            src = f.read()
        
        for line in src.split('\n'):
            question, answer = line.split(';')
            self.questions[question] = {'answer': answer}
        
        self.questions_listed = []
        keys = list(self.questions.keys())
        while keys:
            self.questions_listed.append(keys.pop(randint(0, len(keys) - 1)))
