# app/routes/login.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.login_form import LoginForm
from flask_jwt_extended import create_access_token
from datetime import timedelta

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Simulamos un usuario admin
        if username == "admin" and password == "admin":
            access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("login.success"))

        flash("Credenciales inválidas", "danger")

    return render_template("login.html", form=form)

@login_bp.route("/success")
def success():
    return "Login exitoso."