from BingCloudSearch import CloudySearch
from flask import render_template, redirect, session
from config import BINGAPI

from app import app
from .forms import SearchForm


@app.route('/')
@app.route('/search', methods=['POST', 'GET'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        img = CloudySearch(BINGAPI, form.searchstring.data, form.searchmodifier.data).create_cloud()
        img.savefig('C:\\Users\\Tim\\PycharmProjects\\CloudWordWeb\\app\static\\' + form.searchstring.data)
        session['searchterm'] = form.searchstring.data
        return redirect('/index'),
    return render_template('search.html',
                           title='Search',
                           form=form)


@app.route('/index', methods=['GET', 'POST'])
def index():
    img = 'static/' + session['searchterm'] + ".png"

    return render_template('index.html',
                           title='Home',
                           img=img)
