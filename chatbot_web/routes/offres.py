import os

from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from pathlib import Path
from datetime import datetime

from models.offre import Offre
from config.utils import is_logged_in

offres_blueprint = Blueprint('offres', __name__, url_prefix="/offres")

# GET THE MEDIA PATH
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
parent = Path(APP_ROOT).resolve().parents[0]
TARGET_IMAGES_OFFRE = os.path.join(parent, 'static/offres')


##########################################################################################################################################
# Mobile

@offres_blueprint.route("/mobile")
@is_logged_in
def offres_mobile_index():
    return render_template(
        "offres/mobile/index.html", offres=Offre.read_all('MOBILE')
    )


@offres_blueprint.route("/mobile/details/<offre_id>")
@is_logged_in
def offres_mobile_details(offre_id):
    offre = Offre.read_one(offre_id, "MOBILE")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_mobile_index"))

    return render_template(
        "offres/mobile/details.html", offre=offre
    )


@offres_blueprint.route("/mobile/create", methods=['GET', 'POST'])
@is_logged_in
def offres_mobile_create():
    if request.method == 'POST':

        nom = request.form['nom']
        url = request.form['url']
        sous_categorie = request.form['sous_categorie']
        description = request.form['description']

        # CODE TO UPLOAD IMAGE
        nom_image = ""
        for upload in request.files.getlist("media_photo"):
            image = upload.filename
            if image != "":
                ext = image.split('.')[-1].lower()
                if ext in ["png", "jpg", "jpeg"]:
                    nom_image = datetime.now().strftime("%Y_%m-%d_%H_%M_%S_") + image
                    destination = "/".join([TARGET_IMAGES_OFFRE, nom_image])
                    upload.save(destination)

        Offre.create(nom, url, description, nom_image,
                     "MOBILE", sous_categorie)
        flash('Offre ajoutée avec succés', 'success')
        return redirect(url_for('offres.offres_mobile_index'))

    return render_template(
        "offres/mobile/create.html"
    )


@offres_blueprint.route("/mobile/update/<offre_id>", methods=['GET', 'POST'])
@is_logged_in
def offres_mobile_update(offre_id):
    offre = Offre.read_one(offre_id, "MOBILE")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_mobile_index"))

    if request.method == 'POST':

        nom = request.form['nom']
        url = request.form['url']
        sous_categorie = request.form['sous_categorie']
        description = request.form['description']

        # CODE TO UPLOAD IMAGE
        nom_image = offre.get('media_photo', '')
        for upload in request.files.getlist("media_photo"):
            image = upload.filename
            if image != "":
                ext = image.split('.')[-1].lower()
                if ext in ["png", "jpg", "jpeg"]:
                    nom_image = datetime.now().strftime("%Y_%m-%d_%H_%M_%S_") + image
                    destination = "/".join([TARGET_IMAGES_OFFRE, nom_image])
                    upload.save(destination)

        Offre.update(offre_id, nom, url, description,
                     nom_image, "MOBILE", sous_categorie)
        flash('Offre modifiée avec succés', 'success')
        return redirect(url_for('offres.offres_mobile_details', offre_id=offre_id))

    return render_template(
        "offres/mobile/update.html", offre=offre
    )


@offres_blueprint.route("/mobile/delete/<offre_id>")
@is_logged_in
def offres_mobile_delete(offre_id):
    offre = Offre.read_one(offre_id, "MOBILE")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_mobile_index"))

    Offre.delete(offre_id)
    flash('Offre supprimée avec succés', 'success')
    return redirect(url_for("offres.offres_mobile_index"))

##########################################################################################################################################


##########################################################################################################################################
# Internet

@offres_blueprint.route("/internet")
@is_logged_in
def offres_internet_index():
    return render_template(
        "offres/internet/index.html", offres=Offre.read_all('INTERNET')
    )


@offres_blueprint.route("/internet/details/<offre_id>")
@is_logged_in
def offres_internet_details(offre_id):
    offre = Offre.read_one(offre_id, "INTERNET")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_internet_index"))

    return render_template(
        "offres/internet/details.html", offre=offre
    )


@offres_blueprint.route("/internet/create", methods=['GET', 'POST'])
@is_logged_in
def offres_internet_create():
    if request.method == 'POST':

        nom = request.form['nom']
        url = request.form['url']
        sous_categorie = request.form['sous_categorie']
        description = request.form['description']

        # CODE TO UPLOAD IMAGE
        nom_image = ""
        for upload in request.files.getlist("media_photo"):
            image = upload.filename
            if image != "":
                ext = image.split('.')[-1].lower()
                if ext in ["png", "jpg", "jpeg"]:
                    nom_image = datetime.now().strftime("%Y_%m-%d_%H_%M_%S_") + image
                    destination = "/".join([TARGET_IMAGES_OFFRE, nom_image])
                    upload.save(destination)

        Offre.create(nom, url, description, nom_image,
                     "INTERNET", sous_categorie)
        flash('Offre ajoutée avec succés', 'success')
        return redirect(url_for('offres.offres_internet_index'))

    return render_template(
        "offres/internet/create.html"
    )


@offres_blueprint.route("/internet/update/<offre_id>", methods=['GET', 'POST'])
@is_logged_in
def offres_internet_update(offre_id):
    offre = Offre.read_one(offre_id, "INTERNET")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_internet_index"))

    if request.method == 'POST':

        nom = request.form['nom']
        url = request.form['url']
        sous_categorie = request.form['sous_categorie']
        description = request.form['description']

        # CODE TO UPLOAD IMAGE
        nom_image = offre.get('media_photo', '')
        for upload in request.files.getlist("media_photo"):
            image = upload.filename
            if image != "":
                ext = image.split('.')[-1].lower()
                if ext in ["png", "jpg", "jpeg"]:
                    nom_image = datetime.now().strftime("%Y_%m-%d_%H_%M_%S_") + image
                    destination = "/".join([TARGET_IMAGES_OFFRE, nom_image])
                    upload.save(destination)

        Offre.update(offre_id, nom, url, description,
                     nom_image, "INTERNET", sous_categorie)
        flash('Offre modifiée avec succés', 'success')
        return redirect(url_for('offres.offres_internet_details', offre_id=offre_id))

    return render_template(
        "offres/internet/update.html", offre=offre
    )


@offres_blueprint.route("/internet/delete/<offre_id>")
@is_logged_in
def offres_internet_delete(offre_id):
    offre = Offre.read_one(offre_id, "INTERNET")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_internet_index"))

    Offre.delete(offre_id)
    flash('Offre supprimée avec succés', 'success')
    return redirect(url_for("offres.offres_internet_index"))

##########################################################################################################################################


##########################################################################################################################################
# Fixe

@offres_blueprint.route("/fixe")
@is_logged_in
def offres_fixe_index():
    return render_template(
        "offres/fixe/index.html", offres=Offre.read_all('FIXE')
    )


@offres_blueprint.route("/fixe/details/<offre_id>")
@is_logged_in
def offres_fixe_details(offre_id):
    offre = Offre.read_one(offre_id, "FIXE")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_fixe_index"))

    return render_template(
        "offres/fixe/details.html", offre=offre
    )


@offres_blueprint.route("/fixe/create", methods=['GET', 'POST'])
@is_logged_in
def offres_fixe_create():
    if request.method == 'POST':

        nom = request.form['nom']
        url = request.form['url']
        sous_categorie = request.form['sous_categorie']
        description = request.form['description']

        # CODE TO UPLOAD IMAGE
        nom_image = ""
        for upload in request.files.getlist("media_photo"):
            image = upload.filename
            if image != "":
                ext = image.split('.')[-1].lower()
                if ext in ["png", "jpg", "jpeg"]:
                    nom_image = datetime.now().strftime("%Y_%m-%d_%H_%M_%S_") + image
                    destination = "/".join([TARGET_IMAGES_OFFRE, nom_image])
                    upload.save(destination)

        Offre.create(nom, url, description, nom_image,
                     "FIXE", sous_categorie)
        flash('Offre ajoutée avec succés', 'success')
        return redirect(url_for('offres.offres_fixe_index'))

    return render_template(
        "offres/fixe/create.html"
    )


@offres_blueprint.route("/fixe/update/<offre_id>", methods=['GET', 'POST'])
@is_logged_in
def offres_fixe_update(offre_id):
    offre = Offre.read_one(offre_id, "FIXE")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_fixe_index"))

    if request.method == 'POST':

        nom = request.form['nom']
        url = request.form['url']
        sous_categorie = request.form['sous_categorie']
        description = request.form['description']

        # CODE TO UPLOAD IMAGE
        nom_image = offre.get('media_photo', '')
        for upload in request.files.getlist("media_photo"):
            image = upload.filename
            if image != "":
                ext = image.split('.')[-1].lower()
                if ext in ["png", "jpg", "jpeg"]:
                    nom_image = datetime.now().strftime("%Y_%m-%d_%H_%M_%S_") + image
                    destination = "/".join([TARGET_IMAGES_OFFRE, nom_image])
                    upload.save(destination)

        Offre.update(offre_id, nom, url, description,
                     nom_image, "FIXE", sous_categorie)
        flash('Offre modifiée avec succés', 'success')
        return redirect(url_for('offres.offres_fixe_details', offre_id=offre_id))

    return render_template(
        "offres/fixe/update.html", offre=offre
    )


@offres_blueprint.route("/fixe/delete/<offre_id>")
@is_logged_in
def offres_fixe_delete(offre_id):
    offre = Offre.read_one(offre_id, "FIXE")
    if not offre:
        flash("Offre non trouvée", "danger")
        return redirect(url_for("offres.offres_fixe_index"))

    Offre.delete(offre_id)
    flash('Offre supprimée avec succés', 'success')
    return redirect(url_for("offres.offres_fixe_index"))

##########################################################################################################################################
