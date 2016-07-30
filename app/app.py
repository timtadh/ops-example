from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return "<html><body><h1>Hello World</h1></body></html>"
