import webapp2
from google.appengine.api import users
from utils import template
from wrappers.auth import login_required
from models.comment import Comment

class ContentHandler(webapp2.RequestHandler):

    def get(self, content_id):
        user = users.get_current_user()
        comments = Comment.get_by_content_id(content_id)
        params = {
            'user': user,
            'content_id': content_id,
            'comments': comments
        }
        self.response.write(template.render('content/' + content_id + '.html', params))


class CommentHandler (webapp2.RequestHandler):

    @login_required
    def post(self, content_id):
        user = users.get_current_user()
        comment = {
            'nickname': user.nickname(),
            'content_id': content_id,
            'comment': self.request.get('comment')
        }
        Comment.create(comment)
        self.redirect('/content/' + content_id + "?action=comment.post")

    @login_required
    def delete(self, content_id, comment_id):
        comment = Comment.get(int(comment_id))
        comment.delete()
        self.redirect('/content/' + content_id + "?action=comment.delete")
