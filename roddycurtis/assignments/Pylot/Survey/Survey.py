
from system.core.controller import *

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)
      
    def index(self):

     return self.load_view('index.html')
     

    def process(self):
     print 'top'
     data= {
     'name':request.form['name'],
     'locations':request.form['locations'],
     'language':request.form['language'],
     'description':request.form['description']
     }
     print 'hello'
     return self.load_view('process.html',data=data)

