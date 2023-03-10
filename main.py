'''
write a basic flask app that returns a json object with the following information:
- messier number
- ngc number
- typr
- magnitude
- size
- distance
- RA
- DEC
- constellation
- season
- common name

the app should have the following routes:
- /messier/<messier_number>
- /messier/random
- /messier

the /messier route should return a list of all messier objects
the /messier/random route should return a random messier object
the /messier/<messier_number> route should return the messier object with the given number

the app should scrape the data from the following url:
http://astropixels.com/messier/messiercat.html starting from the table body

the json object should be returned as a response to the request
'''

from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

@app.route('/messier')
def messier():
    return jsonify(messier_objects)
    

@app.route('/messier/random')
def random_messier():
    return jsonify(random.choice(messier_objects))

@app.route('/messier/<messier_number>')
def messier_number(messier_number):
    for messier_object in messier_objects:
        if messier_object['messier_number'] == messier_number:
            return jsonify(messier_object)
    return jsonify({'error': 'Messier object not found'})

if __name__ == '__main__':
    url = 'http://astropixels.com/messier/messiercat.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')
    messier_objects = []
    '''
    strip newlines and spaces from the data
    '''

    for table_row in table_rows:
        table_data = table_row.find_all('td')
        messier_number = table_data[0].text.strip()
        ngc_number = table_data[1].text.strip()
        type = table_data[2].text.strip()
        magnitude = table_data[3].text.strip()
        size = table_data[4].text.strip()
        distance = table_data[5].text.strip()
        ra = table_data[6].text.strip()
        dec = table_data[7].text.strip()
        constellation = table_data[8].text.strip()
        season = table_data[9].text.strip()
        common_name = table_data[10].text.strip()
        messier_object = {
            'messier_number': messier_number,
            'ngc_number': ngc_number,
            'type': type,
            'magnitude': magnitude,
            'size': size,
            'distance': distance,
            'ra': ra,
            'dec': dec,
            'constellation': constellation,
            'season': season,
            'common_name': common_name
        }
        messier_objects.append(messier_object)
    app.run(debug=True)

