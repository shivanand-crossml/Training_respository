car =  {"brand":"Honda",
        "model":"Civic",
        "year":"15/06/2000",
        "price":"30000000"
        }

for key, value in car.items():
    print(key, ' : ', value)

print(f"The {car['brand']} {car['model']} was made in {car['year']} and costs ${car['price']}")