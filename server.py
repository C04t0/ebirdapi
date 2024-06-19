
from urllib.error import HTTPError, URLError
from flask import Flask, render_template, url_for, request, redirect

#own ebird api
from source.database import Database

#found ebird api
from ebird.api import Client
from ebird.api import get_hotspot
from ebird.api import get_observations

app = Flask(__name__)
api_key = '2hig7s0jt391'
database = Database('birds.db')
ebird_api_client = Client(api_key, 'en')


@app.route('/')
def index():
    try:
        return render_template('index.html', title='EBird API')
    except Exception as e:
        return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())


@app.route('/about')
def about():
    try:
        return render_template('about.html', title="About")
    except Exception as e:
        return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())


@app.route('/regions')
def regions():
    region = ebird_api_client.get_region("BE-VLG")
    print(region)
    return render_template('regions.html', title='Regions', region=region)


@app.route('/regions/detail', methods=['GET', 'POST'])
def region_detail():
    if request.method == 'POST':
        region_id = request.form.get('region_id')
        try:
            region = ebird_api_client.get_region(region_id)
            return render_template('region_detail.html', title='Regions', region=region, region_id=region_id)
        except Exception as e:
            return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())
    return render_template('region_detail.html', title='Region Details')


@app.route('/regions/adjacent', methods=['GET', 'POST'])
def adjacent_regions():
    if request.method == 'POST':
        region_type = request.form.get('region_type')
        region_name = request.form.get('region_name')
        try:
            region_list = ebird_api_client.get_regions(region_type, region_name)
            return render_template('adjacent_regions.html', title='Adjacent Regions', region_type=region_type,
                                   region_name=region_name, region_list=region_list)
        except Exception as e:
            return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())
    return render_template('adjacent_regions.html', title='Adjacent Regions')


@app.route('/hotspots')
def hotspots():
    try:
        locations = database.get_locations()
        hotspot = ebird_api_client.get_hotspot(locations[1].region_id)
        return render_template('hotspots.html', title='Hotspots', locations=locations, hotspot=hotspot)
    except HTTPError as e:
        return render_template('error.html', title=f'Error {e.code}', error=e.code)
    except URLError as e:
        return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())


@app.route('/hotspots/detail', methods=['GET', 'POST'])
def hotspot_detail():
    try:
        hotspot = get_hotspot(api_key, 'L13536525')
        return render_template('hotspot-detail.html', title='Hotspots', hotspot=hotspot)
    except Exception as e:
        return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())


@app.route('/species')
def species():
    try:
        species_list = ebird_api_client.get_taxonomy_forms('barswa')
        species_db_list = database.get_species_by_species_code('barswa')
        print(species_list)
        print(species_db_list)
        return render_template('species.html', title='Species', species_list=species_list,
                               species_db_list=species_db_list)
    except Exception as e:
        return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())


@app.route('/species/list', methods=['GET', 'POST'])
def species_list():
    if request.method == 'POST':
        species_code = request.form.get('species_code')
        try:
            species_list = ebird_api_client.get_taxonomy_forms(species_code)
            species_db_list = database.get_species_by_species_code(species_code)
            print(species_list)
            return render_template('species_list.html', title='Species code list', species_list=species_list, species_db_list=species_db_list)
        except HTTPError as e:
            return render_template('error.html', title=f'Error {e.code}', error=e.code)
        except ValueError as e:
            return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())
    return render_template('species_list.html', title='Species code list', species_list=[])

@app.route('/species/detail', methods=['GET', 'POST'])
def species_details():
    if request.method == 'POST':
        common_name = request.form.get('species_name')
        try:
            species_db_list = database.find_species_by_common_name(common_name)
            print(species_db_list)
            return render_template('species_detail.html', title='Species details', species_db_list=species_db_list)
        except HTTPError as e:
            return render_template('error.html', title=f'Error {e.code}', error=e.code)
    return render_template('species_detail.html', title='Species details', species_db_list=[])

@app.route('/species/detail/sci', methods=['GET', 'POST'])
def species_details_sci():
    if request.method == 'POST':
        scientific_name = request.form.get('species_sci_name')
        try:
            species_db_list = database.find_species_by_scientific_name(scientific_name)
            print(species_db_list)
            return render_template('species_detail.html', title='Species details', species_db_list=species_db_list)
        except HTTPError as e:
            return render_template('error.html', title=f'Error {e.code}', error=e.code)
    return render_template('species_detail.html', title='Species details', species_db_list=[])



@app.route('/observations')
def observations():
    try:
        observations = get_observations(api_key, 'L13536525', back=3)
        print(observations)
        return render_template('observations.html', title='Observations', observations=observations)
    except Exception as e:
        return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())

@app.route('/observations/list', methods=['GET', 'POST'])
def observations_list():
    if request.method == 'POST':
        location_id = request.form.get('location_id')
        try:
            observations_list = get_observations(api_key, location_id, back=3)
            print(observations_list)
            return render_template('observations_list.html', title='Observations', observations=observations_list)
        except HTTPError as e:
            return render_template('error.html', title=f'Error {e.code}', error=e.code)
        except Exception as e:
            return render_template('error.html', title=f'Error {e.__class__.__name__}', error=e.__repr__())
    return render_template('observations_list.html', title='Observations', observations_list=[])

@app.route('/checklists')
def checklists():
    return render_template('checklists.html', title='Checklists')

if __name__ == '__main__':
    app.run(debug=True)
