from flask import Blueprint, render_template, request, redirect, url_for, flash
from application.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user, current_user






auth = Blueprint('auth', __name__, template_folder = 'templates')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter(User.email == email).first()
        if user and check_password_hash(password=password, pwhash=user.password_hash):
            login_user(user, remember=remember)
            print(current_user)
            print(current_user.id)
            return redirect('/admin')
        else:
            flash('Wrong password')
            
            return redirect(url_for('auth.login'))

    else:
        return render_template('/auth/login.html')
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

