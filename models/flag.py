from google.appengine.ext import ndb
import json

class Flag(ndb.Model):
    award_id = ndb.StringProperty(required=True, indexed=True)
    user_email = ndb.StringProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)

    def read(self):
        return json.dumps({
            'flag_id': self.id(),
            'award_id': self.award_id,
            'user_email': self.user_email,
            'created_at': self.created_at
        })

    def delete(self):
        self.key.delete()

    @staticmethod
    def create(flag):
        item = Flag(award_id=flag['award_id'],
                       user_email=flag['user_email'])
        item.put()
        return item

    @staticmethod
    def get(flag_id):
        return ndb.Key(Flag, flag_id).get()

    @classmethod
    def get_by_award_email(cls, award_id, email):
        return cls.query(Flag.award_id == award_id, Flag.user_email == email).order(-cls.created_at)