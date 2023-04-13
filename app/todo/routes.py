from flask import Blueprint, render_template, request, current_app

from .models import User

all_cookies = Cookie.query.paginate(page_number, current_app.config['COOKIES_PER_PAGE'])

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

@blueprint.route('/cookies')
def cookies():
  all_cookies = Cookie.query.all()
  return render_template('cookies/index.html', cookies=all_cookies)

@blueprint.route('/cookies')
def cookies():
  page_number = request.args.get('page', 1, type=int)
  cookies_pagination = Cookie.query.paginate(page_number, current_app.config['COOKIES_PER_PAGE'])
  return render_template('cookies/index.html', cookies_pagination=cookies_pagination)