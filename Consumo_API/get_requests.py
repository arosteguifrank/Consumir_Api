# coding=utf-8
import requests
import json

# This example uses Requests HTTP Library

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

API = config['API']['baseUrl']


def categories_all(headers):
    '''
    Returns all categories 
    '''
    url = API + '/api/v2.1/categories'

    # Make get request to API with headers
    response = requests.get(url, headers=headers)
    return response.json()


def categorie_by_id(categorie_id, headers):
    '''
    Returns one categorie by id
    '''
    url = API + '/api/v2.1/categories/{}'.format(categorie_id)

    # Makes get request to API with headers
    response = requests.get(url, headers=headers)
    return response.json()


