import webapp2
from google.appengine.api import users
from utils import template
from wrappers.auth import login_required
from models.api import BidInformationModel, OrganizationModel
from utils import parseutil

NUMPERPAGE = 20

class BidInfoHandler(webapp2.RequestHandler):

    def get(self):
        page = self.request.get('page', '1')
        page = int(page)
        user = users.get_current_user()
        bidinfos = BidInformationModel.get_many(limit=NUMPERPAGE, offset=(page-1)*NUMPERPAGE)
        params = {
            'user': user,
            'bidinfos': bidinfos,
            'page': page
        }
        self.response.write(template.render('bidinfo/list.html', params))

    def get_one(self, ref_id):
        user = users.get_current_user()
        bidinfo = BidInformationModel.getOne(ref_id)
        bidinfo = bidinfo[0]
        lineitems = BidInformationModel.getLineItems(ref_id)
        org = OrganizationModel.getOne(bidinfo['org_id'])
        org = org[0]
        print bidinfo
        for key, val in bidinfo.items():
            bidinfo[key] = parseutil.process(val)

        params = {
            'user': user,
            'bidinfo': bidinfo,
            'org': org,
            'lineitems': lineitems
        }
        self.response.write(template.render('bidinfo/item.html', params))

    def get_line_item(self, ref_id, line_item_id):
        user = users.get_current_user()
        bidinfo = BidInformationModel.getOne(ref_id)
        bidinfo = bidinfo[0]
        org = OrganizationModel.getOne(bidinfo['org_id'])
        org = org[0]
        lineitem = BidInformationModel.getLineItem(ref_id, line_item_id)
        lineitem = lineitem[0]
        print bidinfo
        params = {
            'user': user,
            'bidinfo': bidinfo,
            'org': org,
            'lineitem': lineitem
        }
        self.response.write(template.render('bidinfo/line_item.html', params))
