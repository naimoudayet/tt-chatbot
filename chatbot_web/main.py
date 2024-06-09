from flask import Flask

from routes.dashboard import dashboard_blueprint
from routes.users import users_blueprint
from routes.faq import faq_blueprint
from routes.clients import clients_blueprint
from routes.agences import agences_blueprint
from routes.offres import offres_blueprint


app = Flask(__name__)
app.secret_key = "r7B!kP2t@3Z$qLw8sF5hG*mA"

# LOGIN/LOGOUT/PROFIL
app.register_blueprint(users_blueprint)
# DASHBOARD
app.register_blueprint(dashboard_blueprint)
# FAQ
app.register_blueprint(faq_blueprint)
# CLIENTS
app.register_blueprint(clients_blueprint)
# AGENCES
app.register_blueprint(agences_blueprint)
# OFFRES
app.register_blueprint(offres_blueprint)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
