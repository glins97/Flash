from random import choice

class Flasher(object):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename
        self.questions = {}
        self.q_keys = []
        self.state = 'q'
        self.screen = None
        self.load()

    def next(self):
        if self.state == 'q':
            self.state = 'a'
            self.screen.show_answer();            

        elif self.state == 'a':
            self.state = 'q'
            self.screen.update_set()
            self.screen.show_question();            

    def request_set(self):
        q = self.request_question()
        a = self.request_answer(q)
        return q, a
        
    def request_question(self):
        return choice(self.q_keys)

    def request_answer(self, question):
        return self.questions[question]['answer']

    def keyboard_hook(self, window, key, *largs):
        if key == 13 or key == 271: # enter
            self.next()

    def load(self):
        self.questions = {}
        src = ''

        with open(self.filename) as f:
            src = f.read()
        
        for line in src.split('\n'):
            question, answer = line.split(';')
            self.questions[question] = {'answer': answer}
        
        self.q_keys = list(self.questions.keys())
