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
import pandas as pd
import time

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) #skip header
        for row in reader:
            designation = row[3]
            name = row[2]
            hazardous = row[7]
            diameter = row[15]
            if designation == '' or designation is None:
                designation = ''
            if name == '' or name is None:
                name = ''
            if diameter == '' or diameter is None:
                diameter = float('nan')
            else:
                diameter = float(diameter)
            if hazardous == 'N':
                hazardous = False
            else:
                hazardous = True
            neos.append(NearEarthObject(designation=designation,
                                        name=name,
                                        diameter=diameter,
                                        hazardous=hazardous))
    return neos
            
## To get basic info about data, in prod environment I would use pandas instead of built-in libraries.
#     neo_df = pd.read_csv(neo_csv_path)
#     pd.set_option('display.max_columns', None)
#     print(neo_df.head()) 

            


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    caps = []
    with open(cad_json_path, 'r') as f:
        data = json.load(f)
        for item in data['data']:
            designation = item[0]
            time = item[3]
            distance = item[4]
            velocity = item[7]
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
