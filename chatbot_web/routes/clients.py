from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from config.utils import is_logged_in

clients_blueprint = Blueprint('clients', __name__, url_prefix="/clients")


@clients_blueprint.route("/")
@is_logged_in
def clients_index():
    return render_template(
        "clients/index.html"
    )


@clients_blueprint.route("/details/<id>")
@is_logged_in
def clients_details(id):
    return render_template(
        "clients/details.html"
    )
