"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            designation = row['pdes']
            name = row['name']
            hazardous = (row['pha'] == 'Y')
            diameter = row['diameter']
            
            neos.append(NearEarthObject(designation=designation,
                                        name=name,
                                        diameter=diameter,
                                        hazardous=hazardous))                    
    return neos
                           
            
            


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    caps = []
    with open(cad_json_path, 'r') as f:
        data = json.load(f)
        for item in data['data']:
            item = dict(zip(data['fields'], item))
                           
            designation = item['des']
            time = item['cd']
            distance = item['dist']
            velocity = item['v_rel']
            if distance is not None and distance != '':
                distance = float(distance)
            else:
                distance = float('nan')
                
            if velocity is not None and velocity != '':
                velocity = float(velocity)
            else:
                velocity = float('nan')
            caps.append(CloseApproach(designation=designation,
                                      time=time,
                                      distance=distance,
                                      velocity=velocity))
    return caps
