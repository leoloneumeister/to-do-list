from flask import Blueprint, render_template

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route("/")
def index():
    return render_template("index.html")

@blueprint.route('/playou')
def playou():
    return render_template('logoplayou.html')


@blueprint.route('/notworking')
def notworking():
    return render_template('notworking.html')

@blueprint.route('/about')
def about():
    return render_template('about.html')