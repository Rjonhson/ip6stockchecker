import webapp2
from google.appengine.api import mail
import logging
import urllib2
import json


class CheckerHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("Checker is being invoked")

        logging.debug("Requesting remote URL")
        response = urllib2.urlopen('http://store.apple.com/us/buyFlowSelectionSummary/IPHONE6P_UNLOCKED?node=home/'
                                   'shop_iphone/family/iphone6&step=select&option.dimensionScreensize=5_5inch&'
                                   'option.dimensionColor=space_gray&option.dimensionCapacity=16gb&'
                                   'cppart=TMOBILE%2FUS&carrierPolicyType=UNLOCKED')

        logging.debug("Parsing json")
        result = json.load(response)
        option = result['body']['content']['selected']['purchaseOptions']

        if not "unavailable" in option['shippingLead'] or option['isBuyable']:
            mail.send_mail(sender="<sender>",
                           to="<recipient>",
                           subject="iPhone 6 Plus is now available in US store. Act now!!!",
                           body="Act now.")

        self.response.write('OK')
