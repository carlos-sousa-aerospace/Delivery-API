from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Global variables
stores = [
    {
        "name": "SpaceX",
        "items": [
            {
                "name": "jet propulsor",
                "price": "120450.00",
                "currency": "USD"
            }
        ]
    }
]

# Server perspective:
#    POST: used to receive data from the request
#    GET: used to send data back


# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    try:
        return jsonify(next(s for s in stores if s["name"] == name))
    except StopIteration:
        return jsonify({"Error 407": "Store not found"})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    try:
        store = next(s for s in stores if s["name"] == name)  # StopIteration
        new_item = {
            "name": request_data["name"],
            "price": request_data["price"],
            "currency": request_data["currency"]
            }
        if "items" in store:
            store["items"].append(new_item)
        else:
            store["items"] = new_item
        return jsonify(store["items"])
    except StopIteration:
        return jsonify({"Error 407": "Store not found"})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    try:
        return jsonify(
            {"items": next(s for s in stores if s["name"] == name)["items"]}
            )
    except StopIteration:
        return jsonify({"Error 407": "Store not found"})


# API test route
@app.route("/test")
def test():
    # looks the templates folder by default
    return render_template("index.html")


# Home route
@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"


def init():
    # Run flask dev server
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    init()
