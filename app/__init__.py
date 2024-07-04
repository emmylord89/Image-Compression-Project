from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.config['SECRET_KEY'] = 'your_secret_key'

    from . import routes
    app.register_blueprint(routes.bp)

    return app
