#import the pandas library
import pandas
#Read in the airports data.
airports = pandas.read_csv("airports.dat",header=None,dtype=str)
airports.columns=["id","name","city","country","code","icao","latitdude","longitude","altitude","timezone","dst","timezone_time","type","source"]
# Read in the airlines data.
airlines = pandas.read_csv("airlines.dat",header=None,dtype=str)
#Read in the routes data.
routes = pandas.read_csv("routes.dat",header=None,dtype=str)
routes.columns = ["airline","airline_id","source","source_id","dest","dest_id","codeshare","stops","equipment"]
airports.head()
