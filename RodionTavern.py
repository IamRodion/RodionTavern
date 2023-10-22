from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs.txt")
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(stream_handler)

#logger.info('El bot está encendido')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RodionTavern.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    item_id = db.Column(db.Integer, db.ForeignKey(Item.id))
    price = db.Column(db.Float)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trades')
def trades():
    trades = db.session.query(Trade, User, Item).join(User, Trade.user_id == User.id).join(Item, Trade.item_id == Item.id).add_columns(User.name, User.username, Item.name).all()
    return render_template('trades.html', trades=trades)

@app.route('/users')
def users():
    return render_template('users.html')

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
