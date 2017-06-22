#import the pandas library
import pandas
#Read in the airports data.
airports = pandas.read_csv("airports.dat",header=None,dtype=str)
airports.columns=["id","name","city","country","code","icao","latitdude","longitude","altitude","timezone","dst","timezone_time","type","source"]
# Read in the airlines data.
airlines = pandas.read_csv("airlines.dat",header=None,dtype=str)
airlines.columns = ["id", "name", "alias", "iata", "icao", "callsign", "country", "active"]
# Read in the routes data.
#Read in the routes data.
routes = pandas.read_csv("routes.dat",header=None,dtype=str)
routes.columns = ["airline","airline_id","source","source_id","dest","dest_id","codeshare","stops","equipment"]
# Show the tables
airports.head()
airlines.head()
routes.head()

#Before we can do so, we need to do a bit data cleaning.
routes=routes[routes["airline_id"]!="\\N"]

import math
def haversine(lon1,lat1, lon2, lat2):
	#Convert coordinates to floats
	lon1,lat1,lon2,lat2=[float(lon1),float(lat1),float(lon2),float(lat2)]
	# Convert to radians from degrees.
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # Compute distance.
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c
    return km
def calc_dist(row):
    dist = 0
    try:
        # Match source and destination to get coordinates.
        source = airports[airports["id"] == row["source_id"]].iloc[0]
        dest = airports[airports["id"] == row["dest_id"]].iloc[0]
        # Use coordinates to compute distance.
        dist = haversine(dest["longitude"], dest["latitude"], source["longitude"], source["latitude"])
    except (ValueError, IndexError):
        pass
    return dist
#Calculate the route lengths
route_lengths = routes.apply(calc_dist, axis=1)

# Use the matplotlib
import matplotlib.pyplot as plt
%matplotlib inline

plt.hist(route_lengths, bins=20)




