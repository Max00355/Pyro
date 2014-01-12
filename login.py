from flask import request, render_template, Blueprint, redirect, session, flash, escape
import protect
from mongo import db

login = Blueprint("login", __name__, static_folder="static")

@login.route("/login/", methods=['GET', 'POST'])
def login_():
    if "login" in session:
        return redirect("/")
    if request.method == "POST":
        username = escape(request.form['username'])
        password = protect.protect(request.form['password'])
        if db.members.find_one({"username":username, "password":password}):
            session['login'] = username
            return redirect("/")
        else:
            flash("Login Failed", "error")

    return render_template("login.html")
