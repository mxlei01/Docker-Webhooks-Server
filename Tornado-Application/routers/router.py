import tornado.web
from handlers.docker_webhook_handler import WebHook
from router_settings import settings

# router.py is used to map between different urls to handlers, and also to set different settings

# application is a tornado web application object, that can be used to set handlers, and settings
application = tornado.web.Application([
    # Map the "/" url to main handlers
    (r"/", WebHook),
], **settings)