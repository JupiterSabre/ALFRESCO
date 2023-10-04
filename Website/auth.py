from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Route_Instance
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)

@auth.route("/login-signup", methods=["GET", "POST"])
def login():
    form_type = None
    if request.method == "POST":
        form_type = request.form.get("form_type")
        if form_type == "login":
            email = request.form.get("email")
            password = request.form.get("password")
            user = User.query.filter_by(email=email).first()
            
            if user:
                if check_password_hash(user.password, password):
                    flash("Login Success 🎊", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for("views.home"))
                else:
                    flash("Incorrect password, try again", category="error")
            else:
                flash("Email not in database, have you signed up?", category="error")



        elif form_type == "signup":
            email = request.form.get("signup-email")
            username = request.form.get("username")
            password1 = request.form.get("password1")
            password2 = request.form.get("password2")

            user = User.query.filter_by(email=email).first()
            if user:
                flash("This email has already been registered.", category="error")
            elif len(email) < 4:
                flash("First name must be greater than 3 characters", category="error")
            elif len(username) < 2:
                flash("Username must be greater than 1 character", category="error")
            elif password1 != password2:
                flash("Passwords do not match")
            elif len(password1) < 6:
                flash("Password must be at least 6 characters")
            else:
                new_user = User(email=email, username=username, password=generate_password_hash(password1, method="sha256"))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash("Account created!", category="success")
                return redirect(url_for("views.home"))
    else:
        flash("Invalid form Submission")

    

    return render_template("login-signup.html", user=current_user)


# login_required decorator for routes that require the user to be logged in (which are most things in this project)
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

