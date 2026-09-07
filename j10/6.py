car = {
    "brand" : "saipa",
    "model" : "pride",
    "speed": 20,
    "color": "white"
}

l = [1, 2, 3]

# print(car["brand"])
# print(car["model"])

car["speed"] = 30
car["id"] = "1234567890"

car.pop("id")
car.popitem()

for i in car:
    print(i, ":", car[i])

for x, y in car.items():
    print(x, "->", y)
