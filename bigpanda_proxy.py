import urllib
import requests
import json
from pprint import pprint
from twisted.application.internet import TCPServer
from twisted.application.service import Application
from twisted.web.resource import Resource
from twisted.web.server import Site


url = "https://api.bigpanda.io/data/v2/alerts"
headers = {'Authorization': 'Bearer <PASTE BEARER HEADER KEY HERE>','Content-Type': 'application/json'}


class FormPage(Resource):
    def render_GET(self, request):
        return ''

    def render_POST(self, request):
        pprint(request.__dict__)
        newdata = urllib.unquote_plus(request.content.read())
        newpayload = newdata.replace("payload=", "")
        jsonnewpayload = json.loads(newpayload)
        bigpanda_alert = {
  "app_key": "<PASTE APP KEY HERE>",
  "alerts": [
   {
    "status": "warning",
    "host": jsonnewpayload['log']['name'],
    "timestamp": jsonnewpayload['event']['t'],
    "description": jsonnewpayload['alert']['name'],
    "cluster": jsonnewpayload['host']['hostname'],
    "context": jsonnewpayload['event']['m']
   }
  ]
}
        bigpandamessage = json.dumps(bigpanda_alert)
        r = requests.post(url, data=bigpandamessage, headers=headers)
        return ''


root = Resource()
root.putChild("form", FormPage())
application = Application("Webhook Proxy")
TCPServer(10000, Site(root)).setServiceParent(application)
