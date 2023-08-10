from Assign4 import *



def equals (expected, student):
    expected = expected.replace(" ", "")
    expected = expected.replace("\t", "")
    expected = expected.lower()
    student = student.replace(" ", "")
    student = student.replace("\t", "")
    student = student.lower()
    return expected == student


# --------------- Test 1 - Airport methods ---------------

a1 = Airport("YXU", "London", "Canada")
a2 = Airport("ABC", "Madrid", "Spain")
a2.setCity("Athens")
a2.setCountry("Greece")
t1 = a1.getCode() == "YXU" and a1.getCity() == "London" and a1.getCountry() == "Canada"
t2 = a2.getCode() == "ABC" and a2.getCity() == "Athens" and a2.getCountry() == "Greece"
t3 = equals("YXU (London, Canada)", a1.__repr__()) and equals("ABC (Athens, Greece)", a2.__repr__())

if t1 and t2 and t3:
    print("Test 1 Passed. (Airport methods)")
else:
    print("Test 1 Failed. (Airport methods)")


# --------------- Test 2 - Flight methods ---------------

f1 = Flight("ABC123", a1, a2)
f2 = Flight("BCS101", Airport("ABQ", "Albuquerque", "United States"), Airport("OMA", "Omaha", "United States"))
f3 = Flight("XYZ321", a1, a2)
t1 = f1.getFlightNumber() == "ABC123" and f1.getOrigin() == a1 and f1.getDestination() == a2
t2 = f1 != f2 and f1 == f3
t3 = equals("Flight: ABC123 from London to Athens {international}", f1.__repr__()) and equals("Flight: BCS101 from Albuquerque to Omaha {domestic}", f2.__repr__())
t4 = not(f1.isDomesticFlight()) and f2.isDomesticFlight()



if t1 and t2 and t3 and t4:
    print("Test 2 Passed. (Flight methods)")
else:
    print("Test 2 Failed. (Flight methods)")



# --------------- Test 3 - Exceptions ---------------

t1 = not(loadData("junk.txt", "stuff.txt"))
t2 = len(allAirports) == 0
t3 = False
try:
    Flight("PNT175", "Toronto", "New York")
except TypeError as e:
    if e.__str__().strip().lower() == "the origin and destination must be airport objects":
        t3 = True

if t1 and t2 and t3:
    print("Test 3 Passed. (Exceptions)")
else:
    print("Test 3 Failed. (Exceptions)")


# --------------- Test 4 - loadData() ---------------

t1 = loadData("airports.txt", "flights.txt")
total = 0
for i in allFlights:
    total += len(allFlights[i])

if t1 and len(allAirports) == 37 and total == 146:
    print("Test 4 Passed. (loadData())")
else:
    print("Test 4 Failed. (loadData())")


# --------------- Test 5 - getAirportByCode() ---------------

t1 = getAirportByCode("ORD")

if isinstance(t1, Airport) and t1.getCity() == "Chicago":
    print("Test 5 Passed. (getAirportByCode())")
else:
    print("Test 5 Failed. (getAirportByCode())")



# --------------- Test 6 - findAllCityFlights() ---------------

cf = findAllCityFlights("Toronto")
cfs = ""
for f in cf:
    cfs += f.getFlightNumber() + " "
t1 = isinstance(cf,list) and len(cf) == 13
acodes = ["JRA488", "MCK533", "QGC143", "KPP582", "CFE916", "MGG225", "WCL282", "LZI123", "DDJ597", "CUN974", "HLR281", "PJT823", "AOK874"]
total = 0
for a in acodes:
    if a in cfs:
        total += 1
t2 = total == 13

if t1 and t2:
    print("Test 6 Passed. (findAllCityFlights())")
else:
    print("Test 6 Failed. (findAllCityFlights())")


# --------------- Test 7 - findAllCountryFlights() ---------------

cf = findAllCountryFlights("Brazil")
cfs = ""
for f in cf:
    cfs += f.getFlightNumber() + " "
t1 = isinstance(cf,list) and len(cf) == 15
acodes = ["EIH124", "XGY802", "YZF667", "UWL771", "ZBH196", "APE574", "QFK290", "FFC468", "MOO674", "PJT823", "PBV867", "ONY044", "EWQ950", "VNN918", "ISA009"]
total = 0
for a in acodes:
    if a in cfs:
        total += 1
t2 = total == 15

if t1 and t2:
    print("Test 7 Passed. (findAllCountryFlights())")
else:
    print("Test 7 Failed. (findAllCountryFlights())")


# --------------- Test 8 - findFlightBetween() ---------------

f1 = findFlightBetween(getAirportByCode("PVG"), getAirportByCode("YOW"))
f2 = findFlightBetween(getAirportByCode("LAX"), getAirportByCode("DTW"))
t1 = equals(f1, "Direct Flight: PVG to YOW")
t2 = f2 == -1

if t1 and t2:
    print("Test 8 Passed. (findFlightBetween())")
else:
    print("Test 8 Failed. (findFlightBetween())")


# --------------- Test 9 - findFlightBetween() ---------------

f1 = findFlightBetween(getAirportByCode("DEL"), getAirportByCode("YYZ"))
t1 = isinstance(f1, set) and "SYD" in f1 and "PHL" in f1
print(f1)

if t1:
    print("Test 9 Passed. (findFlightBetween())")
else:
    print("Test 9 Failed. (findFlightBetween())")



# --------------- Test 10 - findReturnFlight() ---------------


f1 = allFlights["YYZ"][1]
f2 = allFlights["BOG"][1]
f3 = allFlights["MEX"][3]
t1 = findReturnFlight(f1)
t2 = findReturnFlight(f2)
t3 = findReturnFlight(f3)
print(t1)
print(t2)
print(t3)

if f1 == t2 and f2 == t1 and t3 == -1:
    print("Test 10 Passed. (findReturnFlight())")
else:
    print("Test 10 Failed. (findReturnFlight())")


