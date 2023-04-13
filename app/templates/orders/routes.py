from flask import Blueprint, render_template

blueprint = Blueprint('orders', __name__)

@blueprint.route('/checkout')
def checkout():
  return render_template('orders/new.html')