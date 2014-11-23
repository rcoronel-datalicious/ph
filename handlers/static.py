import webapp2
from google.appengine.api import users
from utils import template
from wrappers.auth import login_required
from models.comment import Comment

class StaticHandler(webapp2.RequestHandler):

    def get(self, static_id):
        user = users.get_current_user()
        params = {
            'user': user,
            'static_id': static_id
        }
        self.response.write(template.render('static/' + static_id + '.html', params))

