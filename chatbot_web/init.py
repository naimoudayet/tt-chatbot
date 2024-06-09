from models.user import User


User.drop()


User.create(
    nom="admin",
    prenom="admin",
    telephone="98765432",
    email="admin@gmail.com",
    password="admin",
    role="ADMIN",
    etat="ACTIVE"
)
User.create(
    nom="client",
    prenom="client",
    telephone="98765433",
    email="client@gmail.com",
    password="client",
    role="CLIENT",
    etat="ACTIVE"
)

