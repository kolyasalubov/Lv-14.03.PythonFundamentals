def can_reach_gas_station(miles_left, miles_per_gallon, miles_to_pump):
    gallons_left = miles_left / miles_per_gallon
    return gallons_left >= (miles_to_pump / miles_per_gallon)





