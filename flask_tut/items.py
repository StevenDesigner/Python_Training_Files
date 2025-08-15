from flask import Flask, render_template

app = Flask(__name__)

@app.route("/items")
def show_items():
    products = [
        {"name": "Laptop", "price": 850, "stock": True},
        {"name": "Mouse", "price": 25, "stock": True},
        {"name": "Keyboard", "price": 45, "stock": False}
    ]
    return render_template("items.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
