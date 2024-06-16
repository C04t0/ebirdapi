

from flask import Flask, render_template, url_for, request, redirect

from source.ebirdapi import EbirdAPI
from source.location import Location
from source.database import Database

app = Flask(__name__)
database = Database('birds.db')
api_key = "2hig7s0jt391"
Ebird_API = EbirdAPI(api_key)



@app.route('/')
def index():
    return render_template('index.html', title='EBird API')


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/regions')
def regions():
    return render_template('regions.html', title='Regions')


@app.route('/hotspots')
def hotspots():
    return render_template('hotspots.html', title='Hotspots')


@app.route('/hotspots/detail/<string:hotspot_id>', methods=['GET'])
def hotspot_detail(hotspot_id=None):
    hotspot = EbirdAPI.hotspot_info(hotspot_id)
    return render_template('hotspot-detail.html', title='Hotspots', hotspot=hotspot)


@app.route('/species')
def species():
    return render_template('species.html', title='Species')


if __name__ == '__main__':
    app.run(debug=True)
