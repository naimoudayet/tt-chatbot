from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from config.utils import is_logged_in

faq_blueprint = Blueprint('faq', __name__, url_prefix="/faq")


@faq_blueprint.route("/")
@is_logged_in
def faq_index():
    return render_template(
        "faq/index.html"
    )


@faq_blueprint.route("/details/<id>")
@is_logged_in
def faq_details(id):
    return render_template(
        "faq/details.html"
    )
