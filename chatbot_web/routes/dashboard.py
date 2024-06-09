from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session

from config.utils import is_logged_in

dashboard_blueprint = Blueprint('dashboard', __name__)


@dashboard_blueprint.route("/")
@is_logged_in
def index():
    return render_template(
        "index.html"
    )