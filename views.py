from flask import Blueprint, render_templete
main = Blueprint('main', __name__)
@main.route('/')
def index():
    return "<h1> hello world </h1>

