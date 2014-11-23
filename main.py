import webapp2
from handlers.index import IndexHandler
from handlers.home import HomeHandler
from handlers.test import TestHandler
from handlers.content import ContentHandler, CommentHandler
from handlers.email import EmailHandler
from handlers.bidinfo import BidInfoHandler
from handlers.award import AwardHandler, FlagHandler
from handlers.static import StaticHandler

#configuration
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)

app = webapp2.WSGIApplication(
    [
        ('/test', TestHandler),
        ('/', IndexHandler),
        ('/home', HomeHandler),
        ('/index', IndexHandler),
        ('/email', EmailHandler),
        ('/bidinfo', BidInfoHandler),
        webapp2.Route('/bidinfo/<ref_id>', handler=BidInfoHandler, handler_method='get_one', methods='GET'),
        webapp2.Route('/bidinfo/<ref_id>/<line_item_id>', handler=BidInfoHandler, handler_method='get_line_item', methods='GET'),

        ('/award', AwardHandler),
        webapp2.Route('/award/<award_id>', handler=AwardHandler, handler_method='get_one', methods='GET'),
        webapp2.Route('/award/<award_id>/flag', FlagHandler),
        webapp2.Route('/award/<award_id>/flag/<flag_id>/delete', handler=FlagHandler,
                      handler_method='delete', methods='POST'),

        webapp2.Route('/static/<static_id>', StaticHandler),
        webapp2.Route('/content/<content_id>', ContentHandler),
        webapp2.Route('/content/<content_id>/comment', CommentHandler),
        webapp2.Route('/content/<content_id>/comment/<comment_id>/delete', handler=CommentHandler,
                      handler_method='delete', methods='POST')

    ], debug=True)

