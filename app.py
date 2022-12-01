from flask import Flask
from flask_smorest import Api
from db import db
from flask_jwt_extended import JWTManager
from resources.item import blp as ItemBlueprint
from resources.tag import blp as TagBlueprint
from resources.store import blp as StoreBlueprint
app = Flask(__name__)

# def create_app(db_url=None):

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" #db_url or 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


app.config["JWT_SECRET_KEY"] =  "secret_value"
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)
api.register_blueprint(TagBlueprint)

    # return app