# imports from Airport with the purpose of making use of the Airport objects
from Airport import *


# class called Flight in which it provides the flights from one airport to another airport in the other program
class Flight:

    #  create a function for initializing variables for flight number, origin, and destination
    def __init__(self, flightNo, origin, destination):
        # check if both origin and destination are Airport objects
        # if either or both are no airport objects then it raises a type error
        if not isinstance(origin, Airport) or not isinstance(destination, Airport):
            raise TypeError("The origin and destination must be Airport objects")

        # initializing variables for flight number, origin and destination
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination

    # create function for representation of the flight containing the flight number, the origin city, destination city
    def __repr__(self):
        # if the flight is domestic then return that the flight with flight number from a certain origin to a destination is domestic
        # otherwise, if the flight is international
        # then return that the flight with its flight number from a certain origin to a destination is international
        if self.isDomesticFlight() == True:
            return f"Flight: {self._flightNo} from {self._origin.getCity()} to {self._destination.getCity()} {{domestic}}"

        elif self.isDomesticFlight() == False:
            return f"Flight: {self._flightNo} from {self._origin.getCity()} to {self._destination.getCity()} {{international}}"

    # create a function returns the orgin city and the destination are in the same flight
    def __eq__(self, other):
        # check if other is an airport object then it should return true
        # if it is an object then check if origin and destination are the same for both self and other
        # if other is not a flight object then it should return false
        if isinstance(other, Flight):
            return self._origin == other._origin and self._destination == other._destination
        return False

    # create a getter function that returns the flight number
    def getFlightNumber(self):
        return self._flightNo

    # create a getter function that returns the origin
    def getOrigin(self):
        return self._origin

    # create a getter function that returns the destination
    def getDestination(self):
        return self._destination

    # create a function which determines if the flight is domestic or international
    def isDomesticFlight(self):
        #if the origin country is the sane as the destination country then return true, otherwise, return False
        return self._origin.getCountry() == self._destination.getCountry()

    # create a setter function that sets or updates the origin
    def setOrigin(self, origin):
        self._origin = origin

    # create a setter function that sets or updates the destination
    def setDestination(self, destination):
        self._destination = destination
