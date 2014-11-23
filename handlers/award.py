import webapp2
from google.appengine.api import users
from utils import template
from wrappers.auth import login_required
from models.api import AwardModel, BidInformationModel
from models.flag import Flag
from utils import parseutil

NUMPERPAGE = 20

class AwardHandler(webapp2.RequestHandler):

    def get(self):
        page = self.request.get('page', '1')
        page = int(page)
        user = users.get_current_user()
        awards = AwardModel.get_many(limit=NUMPERPAGE, offset=(page-1)*NUMPERPAGE)
        params = {
            'user': user,
            'awards': awards,
            'page': page
        }
        self.response.write(template.render('award/list.html', params))

    def get_one(self, award_id):
        user = users.get_current_user()
        award = AwardModel.getOne(award_id)
        award = award[0]
        bidinfo = BidInformationModel.getOne(award['ref_id'])
        flag = Flag.get_by_award_email(award_id, user.email())
        print '------------------------'
        print flag.get()
        if '_id' in bidinfo:
            for key, val in bidinfo.items():
                bidinfo[key] = parseutil.process(val)

        params = {
            'user': user,
            'award': award,
            'bidinfo': bidinfo,
            'flag': flag.get()
        }
        self.response.write(template.render('award/item.html', params))


class FlagHandler(webapp2.RequestHandler):

    @login_required
    def post(self, award_id):
        user = users.get_current_user()
        flag = {
            'user_email': user.email(),
            'award_id': award_id
        }
        Flag.create(flag)
        self.redirect('/award/' + award_id + "?action=flag.post")

    @login_required
    def delete(self, award_id, flag_id):
        flag = Flag.get(int(flag_id))
        flag.delete()
        self.redirect('/award/' + award_id + "?action=flag.delete")


