from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session, jsonify

from models.agence import Agence

from config.utils import is_logged_in, villes

agences_blueprint = Blueprint('agences', __name__, url_prefix="/agences")


@agences_blueprint.route("/")
@is_logged_in
def agences_index():
    return render_template(
        "agences/index.html"
    )


@agences_blueprint.route("/details/<agence_id>")
@is_logged_in
def stations_details(agence_id):
    agence = Agence.read_one(agence_id)
    if not agence:
        flash("Agence non trouvée", "danger")
        return redirect(url_for("agences.agences_index"))

    return render_template(
        "agences/details.html",
        agence=agence
    )


@agences_blueprint.route('/json')
def agences_json():
    results = Agence.read_all()

    agences = []
    for result in results:
        agences.append(Agence.to_json(result))

    return jsonify(agences)


@agences_blueprint.route("/create", methods=['GET', 'POST'])
@is_logged_in
def agences_create():
    if request.method == 'POST':

        nom = request.form['nom']
        adresse = request.form['adresse']
        ville = request.form['ville']
        num_fixe = request.form['num_fixe']
        num_fax = request.form['num_fax']
        email = request.form['email']
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        if Agence.find_exist(num_fixe, num_fax, email):
            flash('agence déja existe', 'danger')
            return redirect(url_for('agences.agences_create'))
        else:
            Agence.create(nom, adresse, ville, num_fixe,
                          num_fax, email, latitude, longitude)
            flash('agence ajoutée avec succés', 'success')
            return redirect(url_for('agences.agences_index'))

    return render_template(
        "agences/create.html", villes=villes
    )


@agences_blueprint.route("/update/<agence_id>", methods=["GET", "POST"])
@is_logged_in
def agences_update(agence_id):
    agence = Agence.read_one(agence_id)
    if not agence:
        flash("Agence non trouvée", "danger")
        return redirect(url_for("agences.agences_index"))

    if request.method == "POST":
        nom = request.form['nom']
        adresse = request.form['adresse']
        ville = request.form['ville']
        num_fixe = request.form['num_fixe']
        num_fax = request.form['num_fax']
        email = request.form['email']
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        Agence.update(agence_id, nom, adresse, ville, num_fixe,
                      num_fax, email, latitude, longitude)
        flash("Agence modifiée avec succés", "success")
        return redirect(url_for("agences.agences_index", agence_id=agence_id))

    return render_template("agences/update.html", agence=agence, villes=villes)


@agences_blueprint.route("/delete/<agence_id>")
@is_logged_in
def agences_delete(agence_id):
    agence = Agence.read_one(agence_id)
    if not agence:
        flash("Agence non trouvée", "danger")
        return redirect(url_for("agences.agences_index"))

    Agence.delete(agence_id)
    flash("Agence supprimée avec succés", "success")
    return redirect(url_for("agences.agences_index"))
