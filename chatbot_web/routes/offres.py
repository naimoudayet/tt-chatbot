from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from config.utils import is_logged_in

offres_blueprint = Blueprint('offres', __name__, url_prefix="/offres")


@offres_blueprint.route("/")
@is_logged_in
def offres_index():
    return render_template(
        "offres/index.html"
    )


@offres_blueprint.route("/details/<id>")
@is_logged_in
def offres_details(id):
    return render_template(
        "offres/details.html"
    )
