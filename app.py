from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'elcruzo_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    current_price = db.Column(db.Float)
    target_price = db.Column(db.Float)
    user_id = db.Column(db.String(80), db.ForeignKey('user.id'))
    


login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user1': {'password': 'password123'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

products = [
    {"id": 1, "name": "Laptop", "current_price": 1000.0, "target_price": 900.0},
    {"id": 2, "name": "Smartphone", "current_price": 500.0, "target_price": 450.0},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/track/<int:product_id>', methods=['POST'])
@login_required
def track_product(product_id):
    target_price = float(request.form['target_price'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
