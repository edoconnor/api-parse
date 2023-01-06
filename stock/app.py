import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'dow.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    employee = db.Column(db.Integer)
    mktcap = db.Column(db.Integer)
    revenue = db.Column(db.Integer)
    profit = db.Column(db.Integer)

    def __repr__(self):
        return f'<Stock {self.symbol}>'


@app.route('/')
def index():
    stocks = Stock.query.all()
    return render_template('index.html', stocks=stocks)
