from flask import Flask
from tool import pages # import blueprint called pages 


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)

    return app