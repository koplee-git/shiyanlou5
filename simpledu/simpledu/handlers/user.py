from flask import Blueprint, render_template
from simpledu.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    users = User.query.filter_by(username=username).first()
    return render_template('user.html',users=users)

