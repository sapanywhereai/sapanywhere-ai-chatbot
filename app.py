#!/usr/bin/env python

import urllib
import json
import os
import anw

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)
#anw.init()



@app.route('/webhook', methods=['POST', 'GET'] )
def webhook():
    req = request.get_json(silent = True, force = True)

    print("Request:")
    print(json.dumps(req, indent = 4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent = 4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "lead.create":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    customer = parameters.get("customer")


    speech = "Create sales lead for customer " + customer

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }



if __name__ == '__main__':

    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

#    customers = anw.topN('Customers', 5)
#    print customers[0].get('displayName')


    app.run(debug = True, port = port, host = '127.0.0.1')
