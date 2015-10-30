from tornado.httpclient import AsyncHTTPClient
from tornado import gen, escape
import urllib

# coroutines.py has all the coroutines (async calls), for our handlers

@gen.coroutine
def post_slack_coroutine(url, payload):
    # Usage:
    #       This coroutine will post to a URL with a payload
    # Arguments:
    #       url     : a single url for post request, for example, slack's webhook URL
    #       payload : a json format data that we will used to encode and sent it off
    # Return:
    #       None

    # Create an AsyncHTTPClient for async calls
    http_client = AsyncHTTPClient()

    # Yield the fetch of http_client so that the ioloop can do other things
    response = yield http_client.fetch(url, method="POST", body=payload, headers=None)

    # Return the response
    raise gen.Return(response)