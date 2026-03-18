import pandas as pd
import random

data = []

for i in range(1000):
    area = random.randint(500, 3000)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    floors = random.randint(1, 3)
    parking = random.randint(0, 2)
    location_score = random.randint(1, 10)
    nearby_hospitals = random.randint(0, 5)
    furnished = random.randint(0, 1)

    material_quality = random.randint(1, 10)
    location_type = random.randint(0, 1)  # 0 = village, 1 = city

    price = (
        area * 3000 +
        bedrooms * 500000 +
        bathrooms * 300000 +
        floors * 200000 +
        parking * 100000 +
        location_score * 150000 +
        nearby_hospitals * 70000 +
        furnished * 400000 +
        material_quality * 200000 +
        location_type * 1000000
    )

    data.append([
        area, bedrooms, bathrooms, floors,
        parking, location_score, nearby_hospitals,
        furnished, material_quality, location_type, price
    ])

columns = [
    'area','bedrooms','bathrooms','floors',
    'parking','location_score','nearby_hospitals',
    'furnished','material_quality','location_type','price'
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("house_data_1000.csv", index=False)

print("Updated dataset ready ")