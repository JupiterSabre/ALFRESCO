from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Route_Instance
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer




auth = Blueprint("auth", __name__)

@auth.route("/login-signup", methods=["GET", "POST"])
def login():
    s = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])

    form_type = None
    if request.method == "POST":
        form_type = request.form.get("form_type")
        # login request form config
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


        # Sign up request form config
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
            
            
        # Password reset request
        elif form_type == "request_reset":
            email = request.form.get("res-email")
            user = User.query.filter_by(email=email).first()
            if user:
                token = s.dumps(email, salt="password-reset")
                flash(f"Your token is {token}. Use it to reset your password.")
            else:
                flash("Email not found!", "danger")
            return render_template("login-signup.html", user=current_user)
        
        elif form_type == "reset_password":
            token = request.form.get("reset_token")
            try:
                email = s.loads(token, sale="password-reset", max_age=3600)
                user = User.query.filter_by(email=email).first()
            except:
                flash("The token is invalid or has expired!", "danger")
                return render_template("login-signup.html", user=current_user)
            
            new_password = request.form.get("new_password")
            user.password = generate_password_hash(new_password, method="sha256")
            db.session.commit()
            flash("Password successfully updated", "success")
            return redirect(url_for("auth.login-signup"))
    else:
        flash("Invalid form Submission")
    return render_template("login-signup.html", user=current_user)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TO DO , FIX PASSWORD RESET.
# login_required decorator for routes that require the user to be logged in (which are most things in this project)
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

