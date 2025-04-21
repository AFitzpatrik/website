#když mám ve složce __init__.py, tak se složka bere jako modul(package/balíček)
from flask import Flask

#Zdefinování funkce create_app, která vytvoří a vrátí instanci Flask aplikace. Založení Flask aplikace
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'

    from .views import views

    return app