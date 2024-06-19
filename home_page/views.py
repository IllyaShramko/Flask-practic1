import flask, os
from .models import Product
from project.settings import DATABASE

def render_home():
    if flask.request.method == "POST":
        try:
            product = Product(
                name = flask.request.form['name']
            )

            image = flask.request.files['image']
            image.save(os.path.abspath(__file__ + f"/../../shop_page/static/images/{flask.request.form['name']}.png"))
            print(flask.request.form['name'])
            DATABASE.session.add(product)
            DATABASE.session.commit()
        except Exception as e:
            print(e)
    return flask.render_template("home.html")