from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from models.user import User
from models.facture import Facture
from config.utils import is_logged_in

clients_blueprint = Blueprint('clients', __name__, url_prefix="/clients")


@clients_blueprint.route("/")
@is_logged_in
def clients_index():
    return render_template(
        "clients/index.html", clients=User.read_all()
    )


@clients_blueprint.route("/details/<client_id>")
@is_logged_in
def clients_details(client_id):
    client = User.read_one(client_id, "CLIENT")
    if not client:
        flash("Client non trouvée", "danger")
        return redirect(url_for("clients.clients_index"))

    return render_template(
        "clients/details.html", client=client, factures=Facture.read_all(telephone=client.get('telephone', ''))
    )


@clients_blueprint.route("/update/<client_id>", methods=["GET", "POST"])
@is_logged_in
def clients_update(client_id):
    client = User.read_one(client_id, "CLIENT")
    if not client:
        flash("Client non trouvée", "danger")
        return redirect(url_for("clients.clients_index"))

    if request.method == "POST":
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        telephone = request.form["telephone"]
        email = request.form["email"]
        etat = request.form["etat"]

        User.update(client_id, nom, prenom, telephone, email, etat)
        flash("Client modifiée avec succés", "success")
        return redirect(url_for("clients.clients_index"))

    return render_template("clients/update.html", client=client)


@clients_blueprint.route("/delete/<client_id>")
@is_logged_in
def clients_delete(client_id):
    client = User.read_one(client_id, "CLIENT")
    if not client:
        flash("Client non trouvée", "danger")
        return redirect(url_for("clients.clients_index"))

    User.delete(client_id)
    flash("Client supprimée avec succés", "success")
    return redirect(url_for("clients.clients_index"))


############################################################################

@clients_blueprint.route("/details/<client_id>/factures/create", methods=['GET', 'POST'])
@is_logged_in
def clients_factures_create(client_id):
    client = User.read_one(client_id, "CLIENT")
    if not client:
        flash("Client non trouvée", "danger")
        return redirect(url_for("clients.clients_index"))

    if request.method == 'POST':

        montant = request.form['montant']
        date_facture = request.form['date_facture']

        Facture.create(client.get('telephone', ''), montant, '', date_facture)
        flash('Facture ajoutée avec succés', 'success')
        return redirect(url_for('clients.clients_details', client_id=client_id))

    return render_template(
        "factures/create.html", client_id=client_id
    )


@clients_blueprint.route("/details/<client_id>/factures/update/<facture_id>", methods=['GET', 'POST'])
@is_logged_in
def clients_factures_update(client_id, facture_id):
    client = User.read_one(client_id, "CLIENT")
    if not client:
        flash("Client non trouvée", "danger")
        return redirect(url_for("clients.clients_index"))

    facture = Facture.read_one(facture_id)
    if not facture:
        flash("Facture non trouvée", "danger")
        return redirect(url_for('clients.clients_details', client_id=client_id))

    if request.method == 'POST':

        montant = request.form['montant']
        etat = request.form['etat']
        date_paiement = request.form['date_paiement']
        date_facture = request.form['date_facture']

        Facture.update(
            facture_id,
            client.get('telephone', ''),
            montant,
            etat,
            date_paiement,
            date_facture
        )
        flash('Facture modifiée avec succés', 'success')
        return redirect(url_for('clients.clients_details', client_id=client_id))

    return render_template(
        "factures/update.html", client_id=client_id, facture=facture
    )


@clients_blueprint.route("/details/<client_id>/factures/delete/<facture_id>")
@is_logged_in
def clients_factures_delete(client_id, facture_id):
    client = User.read_one(client_id, "CLIENT")
    if not client:
        flash("Client non trouvée", "danger")
        return redirect(url_for("clients.clients_index"))

    facture = Facture.read_one(facture_id)
    if not facture:
        flash("Facture non trouvée", "danger")
        return redirect(url_for('clients.clients_details', client_id=client_id))

    Facture.delete(facture_id)
    flash('Facture supprimée avec succés', 'success')
    return redirect(url_for('clients.clients_details', client_id=client_id))
