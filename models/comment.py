from google.appengine.ext import ndb
import json

class Comment(ndb.Model):
    content_id = ndb.StringProperty(required=True, indexed=True)
    nickname = ndb.StringProperty(required=True)
    comment = ndb.TextProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)

    def read(self):
        return json.dumps({
            'comment_id': self.id(),
            'content_id': self.content_id,
            'nickname': self.nickname,
            'comment': self.comment,
            'created_at': self.created_at
        })

    def delete(self):
        self.key.delete()

    @staticmethod
    def create(comment):
        item = Comment(content_id=comment['content_id'],
                       nickname=comment['nickname'],
                       comment=comment['comment'])
        item.put()
        return item

    @staticmethod
    def get(comment_id):
        return ndb.Key(Comment, comment_id).get()

    @classmethod
    def get_by_content_id(cls, content_id):
        return cls.query(Comment.content_id == content_id).order(-cls.created_at)