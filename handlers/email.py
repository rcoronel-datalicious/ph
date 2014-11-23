import webapp2
from google.appengine.api import users
from utils import template
from wrappers.auth import login_required
from google.appengine.api import mail
from models.api import BidInformationModel

class EmailHandler(webapp2.RequestHandler):

    @login_required
    def post(self):
        user = users.get_current_user()
        redirect_url = self.request.get('redirect_url')
        message = self.request.get('message')
        id = self.request.get('id') # ref_id
        to = self.request.get('to')
        bidinfo = BidInformationModel.getOne(id)
        bidinfo = bidinfo[0]
        print bidinfo
        email = mail.EmailMessage()
        email.to = to
        email.subject = "[Govt. Procurement] RefID#%s" % bidinfo['ref_id']
        email.sender = "procurementhack@appspot.gserviceaccount.com"
        link = "http://procurementhack.appspot.com/bidinfo/%s" % id
        email.body = """

Hi,

Your friend %s thought you might be interested to bid in this project.

Here are some of the details:

Title: %s
Budget: %s

For more details, please visit this link: %s

Cheers,

Transparent Procurement Team

=======================================================
Message from %s:

%s



        """ % (user.nickname(), bidinfo['tender_title'], bidinfo['approved_budget'], link, user.nickname(), message)



        email.send()

        if redirect_url:
            self.redirect(redirect_url)
        else:
            self.redirect('/')