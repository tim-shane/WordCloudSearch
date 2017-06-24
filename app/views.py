from bing_cloud_search import CloudySearch
from flask import render_template, redirect, session, Flask, flash
from config import BINGAPI, save_image_location
from app import app
from .forms import SearchForm
from urllib.error import URLError

application = Flask(__name__)


@app.route('/')
@app.route('/search', methods=['POST', 'GET'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        session['searchterm'] = form.searchstring.data
        try:
            img = CloudySearch(BINGAPI, form.searchstring.data, form.searchmodifier.data).create_cloud()
            img.savefig(save_image_location + form.searchstring.data + ".png")
            print('Searching for: ' + form.searchstring.data + "(" + form.searchmodifier.data
                  + ")")
            return redirect('/index')
        except URLError as e:
            flash("Crazy server error. Literally insane.")
            print("%s" % e)
            return redirect('/search')
    return render_template('search.html',
                           title='Search',
                           form=form)

@app.route('/index', methods=['GET', 'POST'])
def index():
    img = 'static/' + session['searchterm'] + ".png"
    print("Serving " + session['searchterm'] + ".png")
    return render_template('index.html',
                           title='Home',
                           img=img)
