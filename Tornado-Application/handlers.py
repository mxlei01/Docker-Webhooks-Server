import tornado.web
import json
from executors import executor

# handlers.py contains all the handlers that tornado application uses

# This class is used to handle the main of the webpage
# according to url.py, this handler is mapped to /
# which means the localhost:8888/
class WebHook(tornado.web.RequestHandler):
    def post(self):
        print json.loads(self.request.body)

    def get(self):
        self.write("Hello, world")