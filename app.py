from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "current_price": 1000.0, "target_price": 900.0},
    {"id": 2, "name": "Smartphone", "current_price": 500.0, "target_price": 450.0},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/track/<int:product_id>', methods=['POST'])
def track_product(product_id):
    target_price = float(request.form['target_price'])
    # Logic to save the target price and send price alerts goes here
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)