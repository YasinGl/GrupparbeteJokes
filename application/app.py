from flask import Flask, render_template, request, make_response
import pycountry
import requests

app = Flask(__name__)


def get_country_city_data():
    api_url = 'http://api.citybik.es/v2/networks'
    response = requests.get(api_url)

    country_names = set()
    cities = set()

    if response.status_code == 200:
        data = response.json()
        networks = data.get('networks', [])

        for network in networks:
            location = network.get('location', {})
            country_code = location.get('country', '')
            country = pycountry.countries.get(alpha_2=country_code)
            country_name = country.name if country else 'Unknown Country'
            country_names.add(country_name)
            cities.add(location.get('city', ''))

        return sorted(country_names), sorted(list(cities))

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
    country_names, cities = get_country_city_data()

    stations = []

    if request.method == 'POST':
        country_name = request.form['country']
        if country_name == 'All Countries':
            stations = get_stations_by_country('')
        else:
            country_code = pycountry.countries.lookup(country_name).alpha_2
            stations = get_stations_by_country(country_code)

    return render_template('index.html', stations=stations, countries=country_names, cities=cities)



if __name__ == '__main__':
    app.run(debug=True)