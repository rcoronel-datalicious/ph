import webapp2
from google.appengine.api import users
from utils import template
from wrappers.auth import login_required

class TestHandler(webapp2.RequestHandler):

    def get(self):
        #self.response.write(template.render('d3/test.html', {}))
        self.response.write(template.render('test/email.html', {}))