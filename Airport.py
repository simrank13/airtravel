# class called airport which provides Airport in program with a code, city and country
class Airport:

    # create a function for initializing variables for the code, city and country
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    # create a function to return the representation of the Airport in a format like code(city,country)
    def __repr__(self):
        return f'{self._code}({self._city},{self._country})'

    # create a getter function that returns the airport code
    def getCode(self):
        return self._code

    # create a getter function that returns the airport city
    def getCity(self):
        return self._city

    # create a getter function that returns the airport country
    def getCountry(self):
        return self._country

    # create a setter function that sets or updates the airport city
    def setCity(self, city):
        self._city = city

    # create a setter function that sets or updates the airport country
    def setCountry(self, country):
        self._country = country