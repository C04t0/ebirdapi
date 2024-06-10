from flask import Flask, render_template, url_for, request, redirect

import source.ebirdapi

app = Flask(__name__)
api_key = "2hig7s0jt391"
Ebird_API = source.ebirdapi.EbirdAPI(api_key)
vinderhoutse_bossen = source.location.Location("L13909784", 51.0871423, 3.6546237)
apple_orchard_beiaard = source.location.Location("L30676179", 51.09968, 3.63135)


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
