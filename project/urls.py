import home_page, shop_page
from project.settings import project

home_page.home.add_url_rule(
    rule= '/',
    view_func = home_page.render_home,
    methods = ['POST', "GET"]
)

project.register_blueprint(blueprint=home_page.home)

shop_page.shop.add_url_rule(
    rule= '/shop/',
    view_func = shop_page.render_shop,
    methods = ['POST', "GET"]
)

project.register_blueprint(blueprint=shop_page.shop)
