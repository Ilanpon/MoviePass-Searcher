import json
import requests
import argparse
import os

parser = argparse.ArgumentParser(prog='MPSearcher', description='Checks MoviePass locations')
parser.add_argument('-zip', type=str, nargs='?', default='90210', required=True, help='90210')
args = parser.parse_args()
zipcode = args.zip

request_url = 'https://www.moviepass.com/theaters/zip/{}'.format(zipcode)
r = requests.get(request_url)
contents = r.json()["theaters"]
final_data = []  # stored if we want to do something with the data later
print('Searching zipcode {} \n'.format(zipcode))
for entry in contents:
    movie_theater = '{}, {}, {}, {}, {}, Chain: {}'.format(entry["name"], entry["address"], entry["city"], entry["state"], entry["zip"], entry["theaterChainName"])
    final_data.append(movie_theater)
    print(entry["name"])
    print('{}, {}, {}, {}'.format(entry["address"], entry["city"], entry["state"], entry["zip"]))
    print('Distance: {} miles'.format(entry["distance"]))
    print('Chain: ' + entry["theaterChainName"] + '\n')

