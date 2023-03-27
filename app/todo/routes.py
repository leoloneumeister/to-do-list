from flask import Blueprint, render_template
from .models import User

blueprint = Blueprint("user", __name__)

@blueprint.route("/userlogin")
def dynamictest():
    return render_template('dynamic/userlogin.html')

@blueprint.route("/allusers")
def allusers():
    all_users = User.query.all()
    return render_template("dynamic/showuser.html", users=all_users)

@blueprint.route('/user/<id>')
def induser(id):
    current_user = User.query.filter_by(id=id).first()
    return render_template("dynamic/induser.html", user=current_user )