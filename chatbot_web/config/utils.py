from flask import session, url_for, redirect
from functools import wraps

villes = [
    "Ariana",
    "Beja",
    "Ben Arous",
    "Bizerte",
    "Gabes",
    "Gafsa",
    "Jendouba",
    "Kairouan",
    "Kasserine",
    "Kebili",
    "Kef",
    "Mahdia",
    "Manouba",
    "Medenine",
    "Monastir",
    "Nabeul",
    "Sfax",
    "Sidi Bouzid",
    "Siliana",
    "Sousse",
    "Tataouine",
    "Tozeur",
    "Tunis",
    "Zaghouan",
]


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "_id" in session and session['_id']:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("users.login"))

    return wrap