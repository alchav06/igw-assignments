# ---------------------
# Intersection function
# ---------------------
from osgeo import ogr

def title():
    return "Intersection of two features" # title of the function

def abstract():
    return "A function that intersects two features (line, polygon or point type) and returns the intersected feture in JSON format." # short description of the function

def inputs():
    return [
        ['geom1', 'Input feature','The first geometry feature input.','application/wkt', True],
		['geom2', 'Input feature','The second geometry feature input.','application/wkt', True]	
    ]

def outputs():
    return [['result', 'intersected feature','The feature of the intersection of the two inputs','application/json']]

def execute(parameters):
    featureA = parameters.get('geom1')
    featureB = parameters.get('geom2')

    if (featureA is not None) and (featureB is not None):
        featureA = featureA['value']
        featureB = featureB['value']


    featureA = ogr.CreateGeometryFromWkt(featureA)
    featureB = ogr.CreateGeometryFromWkt(featureB)
    intersection = featureA.Intersection(featureB)	
    print("Content-type: application/json")
    print()
    print(intersection.ExportToJson())
