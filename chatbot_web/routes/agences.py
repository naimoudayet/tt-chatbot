from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from config.utils import is_logged_in

agences_blueprint = Blueprint('agences', __name__, url_prefix="/agences")


@agences_blueprint.route("/")
@is_logged_in
def agences_index():
    return render_template(
        "agences/index.html"
    )


@agences_blueprint.route("/create")
@is_logged_in
def agences_create():
    return render_template(
        "agences/create.html"
    )
