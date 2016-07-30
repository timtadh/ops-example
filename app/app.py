from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return "<html><body><h1>Hello Wizard</h1></body></html>"
