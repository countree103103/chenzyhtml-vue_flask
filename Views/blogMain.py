# -*- coding: utf-8 -*-
from config import *

autoEncoding()

blog_main = Blueprint('b_luyou', __name__, url_prefix='/')


@blog_main.route('/<re("(index.html){0,1}"):empty>', methods=['GET', 'POST'])
def index(empty):
    return render_template('index.html')


@blog_main.route('/gallery', methods=['GET', 'POST'])
def gallery():
    return render_template("gallery.html")


@blog_main.route('/swiper', methods=['GET', 'POST'])
def swiper():
    return render_template("swiper.html")
