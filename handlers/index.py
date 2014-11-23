import webapp2
from google.appengine.api import users
from utils import template

class IndexHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if (user):
            self.redirect('/home')
        else:
            params = {
                'login_url': users.create_login_url(self.request.uri),
                'login': self.request.get('login')
            }
            self.response.write(template.render('index.html', params))
