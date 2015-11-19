import tornado.ioloop
import tornado.web
from routers.router import application

# main.py is the main access point of the tornado app, to run the application, just run "python main.py"

# What this will do is listen to port 8888, and then we can access the app using
# http://localhost:8888 on any browser, or using python requests library
if __name__ == "__main__":
    # Set the application to listen to port 8088
    application.listen(8088)

    # Get the current IOLoop
    currentIOLoop = tornado.ioloop.IOLoop.current()

    # Start the IOLoop
    currentIOLoop.start()