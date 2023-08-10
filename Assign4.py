# import flight and airport objects from Flight and Aiport
from Flight import *
from Airport import *

allAirports = []
allFlights = {}

# create a function called loadData which will load all the data from the airport and flight file
def loadData(airportFile, flightFile):
    # try exception method is used so that both files load properly without errors and exception is used for file not found error when the file is not found
    try:
        # read in all data from the airport and flight file
        airportFile = open(airportFile, "r")
        flightFile = open(flightFile, "r")

        # for every line in airportFile, strip and then split by commas to remove the whitespaces in each line
        # for every word in each line in the airport file, strip each word to remove the whitespaces in each word
        # for each element in each line, strip off the extra spaces
        for line in airportFile:
            line = line.strip().split(",")
            for word in line:
                word = word.strip()
                for element in range(len(line)):
                    line[element] = line[element].strip()
            # create an airport object for code, city and country and add the object to the allAirports list
            allAirports.append(Airport(line[0], line[2], line[1]))

        # for every line in the flightFile, strip and then split by commas to remove the whitespaces in each line
        # for every word in each line in the flight file, strip each word to remove the whitespaces in each word
        # for each element in each line, strip off the extra spaces
        for line in flightFile:
            line = line.strip().split(",")
            for word in line:
                word = word.strip()
                for element in range(len(line)):
                    line[element] = line[element].strip()

             # if the origin is an already existing key in the allFLights dictionary
            # then create Flight objects for flight number, origin's airport code and destination's airport code and append it to the dictionary at the already existing key (origin)
            # otherwise, if the key is not existing, create a new key:value pair for the flight objects
            if line[1] in allFlights:
                allFlights[line[1]].append(Flight(line[0], getAirportByCode(line[1]), getAirportByCode(line[2])))
            else:
                allFlights[line[1]] = [Flight(line[0], getAirportByCode(line[1]), getAirportByCode(line[2]))]
        return True

    except FileNotFoundError:
        return False

# create function to get the airport code
def getAirportByCode(code):
    # for every airport object in the allAirports list
    # check if the airport object's code is the same as the given code, and then return true
    # otherwise return -1 if there is no airport found for the given code
    for airport in allAirports:
        if airport.getCode() == code:
            return airport

    return -1

# create a function to find all the flights for a given city
def findAllCityFlights(city):
    # initialize list which will contain all the flight objects for a given city
    cityFlights = []
    # for each flight object of the values of the allFlights dictionary, iterate through each flight object
    # check if the airports origin or destination city is the same the given city
    #then append the elements to the list and then return the list with the flight object that involve the given city with same as origin ot destination
    for cityFlight in allFlights.values():
        for flight in cityFlight:
            if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city:
                    cityFlights.append(flight)

    return cityFlights

# create a function to find all the flights for a given country
def findAllCountryFlights(country):
    # initialize list which will contain all the flight objects for a given country
    countryFlights = []
    # for each flight object of the values of the allFlights dictionary, iterate through each flight object
    # check if the airports origin or destination country is the same the given country
    # then append the elements to the list and then return the list with the flight object that involve the given country with same as origin ot destination
    for countryFlight in allFlights.values():
        for flight in countryFlight:
            if flight.getOrigin().getCountry() == country  or flight.getDestination().getCountry() == country or (flight.getOrigin().getCountry() == country and flight.getDestination().getCountry() == country):
                countryFlights.append(flight)

    return countryFlights

# create a function to find any flights between the origin airport and the destination airport
def findFlightBetween(origAirport, destAirport):
    # initialize list which will contain code of flight with same origin as origAirport
    code = []
    # create a set which will contain all possible airport codes to serve as the connecting airport from origAirport and destAirport
    connectingAirportSet = set()

    # for each flight object of the values of the allFlights dictionary, iterate through each flight object
    # if the origin airport code is the same as the origAirport's airport code and if the destination airport code is the same as the destAirport's code
    # then return that the direct flight is from a given origAirport's airport code to a given destAirport's airport code
    # however, if the destination airport code is already an existing key then add it to the list containing the airport code
    for i in allFlights.values():
        for findFlights in i:
            if findFlights.getOrigin().getCode() == origAirport.getCode():
                    if findFlights.getDestination().getCode() == destAirport.getCode():
                        return f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"
                    if findFlights.getDestination().getCode() in allFlights.keys():
                        code.append(findFlights.getDestination().getCode())

    # for each airport code in the code list, iterate through the airport code keys in the allFlights dictionary
    # check if the destination city is the same as the destAirport city and then add the airport code to the set containing the airports connecting the origAirport and destAirport
    for airportCode in code:
        for flights in allFlights[airportCode]:
            if flights.getDestination().getCity() == destAirport.getCity():
                connectingAirportSet.add(airportCode)

    #if the set containing the connectAirport is empty this means that there is no direct and no connecting flight and then return -1
    if len(connectingAirportSet) == 0:
        return -1

    return connectingAirportSet

# create a function that will look for a return flight for the given flight
def findReturnFlight(firstFlight):
    # for each of the flight objects of the values in the dictionary, iterate through the objects
    # if the origin's airport code is going in the same direction as the given destination airport code of the given origin flight
    # if the destination's airport code is going in the same direction as the given origin airport code of the given destination flight
    # then return the flight object
    # however if there is no such flight object going in opposite direction as firstFlight then return -1
    for flights in allFlights.values():
        for flight in flights:
            if flight.getOrigin().getCode() == firstFlight.getDestination().getCode():
                if flight.getDestination().getCode() == firstFlight.getOrigin().getCode():
                    return flight

    return -1

#loadData("airports.txt", "flights.txt")
#print(allAirports)
#print(allFlights)
#print(getAirportByCode("ORD"))