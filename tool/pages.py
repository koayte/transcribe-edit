from flask import Blueprint

"""
Create an instance of Blueprint (class) named bp. 
"pages" is the name of blueprint. 
"""
bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return "Hello, Home!"

@bp.route("/about")
def about():
    return "Hello, About!"