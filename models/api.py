import urllib
import json
from google.appengine.api import memcache
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(60)


BASE = 'http://api.data.gov.ph/api/action/datastore_search_sql?'
BIDINFO_TABLE = '9c74991c-a5e6-4489-8413-c20a8a181d90'
BIDLINEITEM_TABLE = '63e29a04-6b13-48f8-ab13-ba72dc9ffcdc'
ORGANIZATION_TABLE = '23de10e9-197e-4294-abd1-eba0188110cd'
AWARD_TABLE = '314aa773-e6e4-4554-80ce-4f588212e0d1'


BASE = 'http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?'
BIDINFO_TABLE = 'baccd784-45a2-4c0c-82a6-61694cd68c9d'
BIDLINEITEM_TABLE = 'daa80cd8-da5d-4b9d-bb6d-217a360ff7c1'
ORGANIZATION_TABLE = 'ec10e1c4-4eb3-4f29-97fe-f09ea950cdf1'
AWARD_TABLE = '539525df-fc9a-4adf-b33d-04747e95f120'


class BidInformationModel():

    @staticmethod
    def get_many(limit=10, offset=0):
        mkey = "bidinfo_getmany_%s_%s" % (limit, offset)
        data = memcache.get(mkey)
        if data:
            return data
        else:
            where = ''
            query= """
    SELECT * FROM "%s" %s ORDER BY creation_date DESC LIMIT %s OFFSET %s
            """ %\
                   (BIDINFO_TABLE, where, limit, offset)
            query = query.rstrip()
            query = query.replace('\n', ' ')
            url = BASE + urllib.urlencode({'sql': query})
            res = urlfetch.fetch(url)
            val = json.loads(res.content)
            memcache.add(mkey, val['result']['records'], 86400)
            return val['result']['records']

    @staticmethod
    def getOne(ref_id):
        mkey = "bidinfo_getone_%s" % ref_id
        data = memcache.get(mkey)
        if data:
            return data
        else:
            query = """
    SELECT * FROM "%s" WHERE ref_id='%s'
            """ %\
                    (BIDINFO_TABLE, ref_id)
            query = query.rstrip()
            query = query.replace('\n', ' ')
            print query
            url = BASE + urllib.urlencode({'sql': query})
            res = urlfetch.fetch(url)
            val = json.loads(res.content)
            memcache.add(mkey, val['result']['records'], 86400)
            return val['result']['records']

    @staticmethod
    def getLineItems(ref_id):
        mkey = "bidinfo_getlineitems_%s" % ref_id
        data = memcache.get(mkey)
        if data:
            return data
        else:
            query = """
    SELECT * FROM "%s" WHERE ref_id='%s'
            """ %\
                    (BIDLINEITEM_TABLE, ref_id)
            query = query.rstrip()
            query = query.replace('\n', ' ')
            print query
            url = BASE + urllib.urlencode({'sql': query})
            res = urlfetch.fetch(url)
            val = json.loads(res.content)
            memcache.add(mkey, val['result']['records'], 86400)
            return val['result']['records']

    @staticmethod
    def getLineItem(ref_id, line_item_id):
        mkey = "bidinfo_getlineitem_%s_%s" % (ref_id, line_item_id)
        data = memcache.get(mkey)
        if data:
            return data
        else:
            query = """
    SELECT * FROM "%s" WHERE ref_id='%s' AND line_item_id='%s'
            """ %\
                    (BIDLINEITEM_TABLE, ref_id, line_item_id)
            query = query.rstrip()
            query = query.replace('\n', ' ')
            print query
            url = BASE + urllib.urlencode({'sql': query})
            res = urlfetch.fetch(url)
            val = json.loads(res.content)
            memcache.add(mkey, val['result']['records'], 86400)
            return val['result']['records']


class OrganizationModel():

    @staticmethod
    def getOne(org_id):
        mkey = "organization_%s" % org_id
        data = memcache.get(mkey)
        if data:
            return data
        else:
            query = """
    SELECT * FROM "%s" WHERE org_id='%s'
            """ %\
                    (ORGANIZATION_TABLE, org_id)
            query = query.rstrip()
            query = query.replace('\n', ' ')
            print query
            url = BASE + urllib.urlencode({'sql': query})
            res = urlfetch.fetch(url)
            val = json.loads(res.content)
            memcache.add(mkey, val['result']['records'], 86400)
            return val['result']['records']

class AwardModel():

    @staticmethod
    def get_many(limit=10, offset=0):
        mkey = "_award_getmany_%s_%s" % (limit, offset)
        data = memcache.get(mkey)
        if data:
            return data
        else:
            where = ''
            query= """
    SELECT * FROM "%s" %s ORDER BY modified_date DESC LIMIT %s OFFSET %s
            """ %\
                   (AWARD_TABLE, where, limit, offset)
            query = query.rstrip()
            query = query.replace('\n', ' ')
            url = BASE + urllib.urlencode({'sql': query})
            res = urlfetch.fetch(url)
            val = json.loads(res.content)
            memcache.add(mkey, val['result']['records'], 86400)
            return val['result']['records']

    @staticmethod
    def getOne(award_id):
        mkey = "award_getone_%s" % award_id
        data = memcache.get(mkey)
        if data:
            return data
        else:
            query = """
    SELECT * FROM "%s" WHERE award_id='%s'
            """ %\
                    (AWARD_TABLE, award_id)
            query = query.rstrip()
            query = query.replace('\n', ' ')
            print query
            url = BASE + urllib.urlencode({'sql': query})
            res = urlfetch.fetch(url)
            val = json.loads(res.content)
            memcache.add(mkey, val['result']['records'], 86400)
            return val['result']['records']
