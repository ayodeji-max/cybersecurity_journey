cities =[
    ("Lagos", "Nigeria", 15000000, 6.5244, 3.3792),
    ("Abuja", "Nigeria", 3600000, 9.0765, 7.3986),
    ("London", "UK", 9000000, 51.5074, -0.1278),
    ("New York", "USA", 8400000, 40.7128, -72.0060),
    ("Nairobi", "Kenya", 4400000, -1.2921, 36.8219)
]

print("All cities:")
for city, country, population, lat, lon in cities:
    print(f"{city}, {country} - Population: {population:,}")

print("\nMost populous city:")
largest =max(cities, key=lambda x: x[2])
print(f"{largest[0]} with {largest[2]:,} people")
