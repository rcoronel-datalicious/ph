from google.appengine.ext import ndb


class User(ndb.Model):
    user_id = ndb.UserProperty(indexed=True)
    nickname = ndb.StringProperty()
    email = ndb.StringProperty()

