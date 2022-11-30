from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


# # @app.get("/store")
# # def get_stores():
    


# @app.post("/store")
# def create_store():
#     store_data = request.get_json(force=True)
#     if "name" not in store_data:
#         abort(404, message="Bad Request")

#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(404, message="Store Already Exists")

#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201


# # @app.get("/store/<string:store_id>")
# # def get_store(store_id):



# # @app.delete("/store/<string:store_id>")
# # def delete_store(store_id):



# @app.post("/item")
# def create_item():
#     item_data = request.get_json(force=True)

#     if (
#         "price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad Request"
#         )

#     for item in items.values():
#         print(item_data["name"], item["name"])
#         if (
#             item_data["name"] == item["name"]
#             and item_data["store_id"] == item["store_id"]
#         ):
#             abort(404, message="Item Already Exists")

#     if item_data["store_id"] not in stores:
#         abort(404, message="Store Not Found")

#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item

#     return item, 201


# @app.get("/item")
# def get_all_items():
    


# @app.get("/item/<string:item_id>")
# def update_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="Item Not Found")


# @app.put("/item/<string:item_id>")
# def get_item(item_id):
#     item_data = request.get_json(force=True)
#     if "price" not in item_data or "name" not in item_data:
#         abort(404, message="Bad Request")
#     try:
#         item = items[item_id]
#         item |= item_data
#         return item
#     except KeyError:
#         abort(404, message="Item Not Found")


# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted"}
#     except KeyError:
#         abort(404, message="Item Not Found")
