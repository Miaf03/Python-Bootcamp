import os
import json
import stripe
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request

load_dotenv()
STRIPE_SECRET = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE = os.getenv("STRIPE_PUBLISHABLE_KEY")
BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")
CURRENCY = os.getenv("CURRENCY", "mxn")

stripe.api_key = STRIPE_SECRET

app = Flask(__name__, static_folder="static", template_folder="templates")

def load_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    products = load_products()
    return render_template("index.html", products=products)

@app.route("/api/products")
def api_products():
    return jsonify(load_products())

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    data = request.get_json()
    cart = data.get("cart", [])
    currency = data.get("currency", CURRENCY).lower()

    if not cart:
        return jsonify({"error": "Cart empty"}), 400

    def to_stripe_amount(amount):
        return int(round(float(amount) * 100))

    line_items = []
    for item in cart:
        qty = int(item.get("quantity", 1))
        unit_amount = to_stripe_amount(item["price"])
        line_items.append({
            "price_data": {
                "currency": currency,
                "product_data": {"name": item["name"]},
                "unit_amount": unit_amount
            },
            "quantity": qty
        })

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=f"{BASE_URL}/success?session_id={{CHECKOUT_SESSION_ID}}",
        cancel_url=f"{BASE_URL}/cancel"
    )
    return jsonify({"url": session.url})

@app.route("/success")
def success():
    session_id = request.args.get("session_id")
    return render_template("success.html", session_id=session_id)

@app.route("/cancel")
def cancel():
    return render_template("cancel.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)