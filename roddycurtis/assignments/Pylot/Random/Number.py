from system.core.controller import *
import random
import string


class Number(Controller):
    def __init__(self, action):
        super(Number, self).__init__(action)


   
    def index(self):
        if not 'random' in session:
            session['number'] = 0
            session['random']=0
            

        else:
            session['number'] += 1

        return self.load_view('index.html',number=session['number'],random=session['random'])

    def process(self):
        print session
        session['random'] = random.randint(1,100)
        session['number'] += 1
       


        return redirect('/')
