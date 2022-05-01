import os

from flask import Flask

from .auth import bp
from .blog import bp as bp_blog

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask_tut.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(bp)

    app.register_blueprint(bp_blog)
    app.add_url_rule('/', endpoint='index')

    from . import db
    db.init_app(app)





    return app