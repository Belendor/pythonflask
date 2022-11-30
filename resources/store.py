from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from schemas import StoreSchema
from models import StoreModel
from db import db

blp = Blueprint("stores", __name__, description = "operations on stores")

@blp.route("/store/<string:store_id>")
@blp.response(200, StoreSchema)
class Store(MethodView):
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store 

    def delete(self, store_id): 
        store = StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("not done yet")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            abort (500, message = "DB Error.")