# to learn more about Python json go to
# https://docs.python.org/3.9/library/json.html

# # run file with python3 filename

# helps make http request for python3

import urllib.request 
import json 

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

        # output the number of events, plus the count for each event name
        count = theJSON["metadata"]["count"]
        print(str(count) + " events recorded")

        # For each event, print the place where it occured
        for i in  theJSON["features"]:
            print(i["properties"]["place"])
        print("------------\n")

        # Print the events that only have a magnitude greater than 4 
        for i in theJSON["features"]:
            if i["properties"]["mag"] >= 4.0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
        print("------------\n")

        # Print only events where at least 1 persone reported feeling something
        print("Events that were felt:")
        for i in theJSON["features"]:
            feltReports = i ["properties"]["felt"]
            if feltReports != None:
                if feltReports > 0:
                    print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
                    " reported " + str(feltReports) + " times")
        print("------------\n")

def main():
    # Define a variable to hold the source URL
    # in this case we will use the free data from USGS
    # this feed list all earthquakes for the last day larger than mag 2.5

    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # 2 - Open Url  & read the data
    webUrl = urllib.request.urlopen(urlData)
    print("earthquake.usgs.gov/earthquakes/feed  HTTP result code is : " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, Could not parse results")


if __name__ == "__main__":
    main()


