# QUESTION 1
# In file cars.json wrote some cars (as array) models with filed
# max_speed. In file cars2.json wrote only one random car (as object)
# with random max_speed. Read both files and write sorted by max_speed
# array of all cars in file result.json. As example if you have file
# cars.json with [ { "model": "Volkswagen Amarok 2.0", "max_speed": 179 },
# { "model": "random_model", "max_speed": 163 } ] and cars2.json
# with {"model": "random_model","max_speed": 91} as result you must
# obtain file result.json with [{"model": "random_model", "max_speed": 91},
# {"model": "random_model", "max_speed": 163},
# {"model": "Volkswagen Amarok 2.0", "max_speed": 179}]

import json
with open("cars.json", "r", encoding="utf-8") as file_cars, \
        open("cars2.json", "r", encoding="utf-8") as file_cars2, \
        open("result.json", "w", encoding="utf-8") as result_file:
    cars = json.load(file_cars)
    car = json.load(file_cars2)
    cars.append(car)
    cars.sort(key=lambda x: x['max_speed'])
    json.dump(cars, result_file)
