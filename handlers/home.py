import webapp2
from google.appengine.api import users
from utils import template
from wrappers.auth import login_required

class HomeHandler(webapp2.RequestHandler):

    @login_required
    def get(self):
        user = users.get_current_user()
        params = {
            'user': user
        }
        self.response.write(template.render('home.html', params))