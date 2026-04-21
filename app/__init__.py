import os
from flask import Flask
from app.database import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'database.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize plugins
    db.init_app(app)

    # Register blueprints
    from app.routes.main import bp as main_bp
    from app.routes.transaction import bp as transaction_bp
    from app.routes.stock import bp as stock_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(stock_bp)

    # Auto-create tables (if not using migrations)
    with app.app_context():
        from app.models import transaction
        from app.models import stock
        db.create_all()

    return app
