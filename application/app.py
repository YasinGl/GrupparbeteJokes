from flask import Flask, render_template, request
import requests
import pycountry

app = Flask(__name__)

def get_country_city_data():
    api_url = 'http://api.citybik.es/v2/networks'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        networks = data.get('networks', [])
        countries = set()
        cities = set()

        for network in networks:
            location = network.get('location', {})
            countries.add(location.get('country', ''))
            cities.add(location.get('city', ''))

        return sorted(list(countries)), sorted(list(cities))

    return [], []

def get_stations_by_country(country_code):
    api_url = 'http://api.citybik.es/v2/networks'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        networks = data.get('networks', [])
        stations = []



        for network in networks:
            location = network.get('location', {})
            if location.get('country') == country_code:
                stations.append(network)

        return stations

@app.route('/', methods=['GET', 'POST'])
def index():
    countries, cities = get_country_city_data()

    stations = []

    if request.method == 'POST':
        country_code = request.form['country']
        if country_code == 'all':
            stations = get_stations_by_country('')
        else:
            stations = get_stations_by_country(country_code)

    return render_template('index.html', stations=stations, countries=countries, cities=cities)

if __name__ == '__main__':
    app.run(debug=True)

#https://www.google.com/maps/embed/v1/view
 # ?key=YOUR_API_KEY
 # &center=-33.8569,151.2152
# &zoom=18
 # &maptype=satellite