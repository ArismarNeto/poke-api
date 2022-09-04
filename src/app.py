from flask import Flask
import biblioteca

def create_app():
    app = Flask("app")
    
    @app.route("/")
    def home():
        return "voce está na página principal"

    @app.route("/alunos")
    def student():
        return "lista todos os alunos"
    
    app.register_blueprint(biblioteca.pb, url_prefix="/biblioteca")
    return app