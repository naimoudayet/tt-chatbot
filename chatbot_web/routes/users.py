from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from models.user import User

from config.utils import is_logged_in

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    # POST
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.login(email, password)
        if user:  # email, password correct
            # . create session
            session["_id"] = str(user["_id"])
            session["nom_prenom"] = f"{user['nom']} {user['nom']}"
            # . redirection page index
            # function of the needed route
            return redirect(url_for("dashboard.index"))
        else:  # email, password incorrect
            # . create error
            flash('email and/or password is incorrect.', 'danger')
            # . redirection page login
            return redirect(url_for("users.login"))

    # GET
    return render_template("login.html")


@users_blueprint.route("/profile")
@is_logged_in
def profile():
    user = User.read_one(session["_id"], "ADMIN")
    if not user:
        return redirect(url_for("users.logout"))
    return render_template("profile.html", user=user)


@users_blueprint.route("/profile/update", methods=["post"])
@is_logged_in
def profile_update():
    user = User.read_one(session["_id"])
    if not user:
        return redirect(url_for("users.logout"))

    nom = request.form["nom"]
    prenom = request.form["prenom"]
    email = request.form["email"]
    telephone = request.form["telephone"]

    User.update(session["_id"], nom, prenom, telephone, email)
    flash("Profil modifié avec succès.", "success")
    return redirect(url_for("users.profil"))


@users_blueprint.route("/profile/update/password", methods=["post"])
@is_logged_in
def profile_update_password():
    user = User.read_one(session["_id"])
    if not user:
        return redirect(url_for("users.logout"))

    ancien_passe = request.form["ancien_passe"]
    nouveau_passe = request.form["nouveau_passe"]
    confirmer_passe = request.form["confirmer_passe"]

    if nouveau_passe == confirmer_passe:
        response = User.update_password(
            session["_id"], ancien_passe, nouveau_passe)
        if response:
            flash("mot de passe modifié avec succès.", "success")
            return redirect(url_for("users.profil"))
        else:
            flash("ancien mot de passe erronée", "danger")
            return redirect(url_for("users.profil"))

    flash("mot de passe non identique.", "danger")
    return redirect(url_for("users.profil"))


@users_blueprint.route("/logout")
@is_logged_in
def logout():
    session.clear()  # delete _id
    return redirect(url_for("users.login"))
