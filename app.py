from flask import Flask
from flask_smorest import Api
from db import db
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from flask import Flask, jsonify
from flask_migrate import Migrate

from resources.item import blp as ItemBlueprint
from resources.tag import blp as TagBlueprint
from resources.store import blp as StoreBlueprint
from resources.user import blp as UserBlueprint

app = Flask(__name__)

# def create_app(db_url=None):

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] =  "postgresql://postgres:1234@localhost:5432/postgres"  #db_url or  #"sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


app.config["JWT_SECRET_KEY"] =  "secret_value"
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (jsonify({"description": "The token has been revoked.","error": "token_revoked"}), 401)

@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {"is_admin" : True}
    return {"is_admin" : False}

# with app.app_context():
#     db.create_all()

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)
api.register_blueprint(TagBlueprint)
api.register_blueprint(UserBlueprint)

    # return app