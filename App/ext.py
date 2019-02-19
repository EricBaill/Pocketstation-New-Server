from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_session import Session
from App.models import db
ma = Marshmallow()

def init_ext(app):
    Session(app=app)
    db.init_app(app=app)
    migrate = Migrate()
    ma.init_app(app)
    migrate.init_app(app=app,db=db)




