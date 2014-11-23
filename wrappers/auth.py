from functools import wraps
from google.appengine.api import users


def login_required(handler_method):
    @wraps(handler_method)
    def check_login(self, *args, **kwargs):
        if not users.get_current_user():
            self.redirect('/index?login=1')
        else:
            handler_method(self, *args, **kwargs)
        return

    return check_login