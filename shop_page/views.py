import flask
from home_page import Product

def render_shop():
    return flask.render_template("shop.html", products = Product.query.all())