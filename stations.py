#!/usr/bin/python

"""Finds a gas station near you."""

import xml.etree.ElementTree as ET

def get_prices():
    """Parse XML.

    Returns:
        (dict) with keys of station ID and values of name, prices, and location info
        '8489': {'name': 'SERVICIOS UNIDOS SA',
                 'prices': {'diesel': '16.06', 'regular': '15.29', 'premium': '17.02'},
                 'address': 'ALTAMIRA NO. 1201 ORIENTE',
                 'y': '22.213',
                 'x': '-97.84769',
                 'id': '8489'}
    """
    stations = {}
    places_tree = ET.parse('places.xml')
    for place in places_tree.getroot():
        station = {}
        station['id'] = place.attrib['place_id']
        station['name'] = place.find('name').text
        station['address'] = place.find('location').find('address_street').text
        station['x'] = place.find('location').find('x').text
        station['y'] = place.find('location').find('y').text
        stations[station['id']] = station

    prices_tree = ET.parse('prices.xml')
    for place in prices_tree.getroot():
        place_id = place.attrib['place_id']
        station_prices = {}
        for price_entry in place:
            price_type = price_entry.attrib['type']
            price = price_entry.text
            station_prices[price_type] = price
            stations[place_id]['prices'] = station_prices

    return stations

def closest_station():
    stations = [{'name': 'SERVICIOS UNIDOS SA',
                 'prices': {'diesel': '16.06', 'regular': '15.29', 'premium': '17.02'},
                 'address': 'ALTAMIRA NO. 1201 ORIENTE',
                 'y': '22.213',
                 'x': '-97.84769',
                 'id': '8489',
                 'distance': 123},
                {'name': 'SERVICIOS UNIDOS SA',
                 'prices': {'diesel': '16.06', 'regular': '15.29', 'premium': '17.02'},
                 'address': 'ALTAMIRA NO. 1201 ORIENTE',
                 'y': '22.213',
                 'x': '-97.84769',
                 'id': '8489',
                 'distance': 124},
                 {'name': 'SERVICIOS UNIDOS SA',
                  'prices': {'diesel': '16.06', 'regular': '15.29', 'premium': '17.02'},
                  'address': 'ALTAMIRA NO. 1201 ORIENTE',
                  'y': '22.213',
                  'x': '-97.84769',
                  'id': '8489',
                  'distance': 2},
               ]
    print sorted(stations, key=lambda station: station['distance'])


def main():
    """Print test."""
    print get_prices()
    print closest_station()


if __name__ == '__main__':
    main()
