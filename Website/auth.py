from flask import Blueprint, render_template, request,flash
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html",text='Testing', )

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) <4:
            flash('Email Name must be greater than 4 characters.', category='error')
        elif re.fullmatch(regex, email):
            flash('The email is not according to the Standard', category='error')
        elif len(firstName)<2:
            flash('First Name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match',category='error')
        elif len(password1)<7:
            flash('Password must be at least 8 characters long.', category='error')
        else:
            flash('Account Created')
    return render_template("sign_up.html") 