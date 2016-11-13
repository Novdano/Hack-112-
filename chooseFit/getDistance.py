import googlemaps
from datetime import datetime

def getDistance():
    gmaps = googlemaps.Client(key='AIzaSyA0xMFw7tA4Oq8tWnArYl5nkFPiJ-qw6Vo')
    
    origin = "Carnegie Mellon University, Pittsburgh"  # user input
    
    destination = "Residence on FIfth, Pittsburgh"     # user input
    matrix = gmaps.distance_matrix(origin, destination)
    
    time = matrix['rows'][0]['elements'][0]['duration']['text']
    distance = matrix['rows'][0]['elements'][0]['distance']['value']
    distance *= 0.000621371   # convert to miles
    return (distance)