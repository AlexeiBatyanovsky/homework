# Дан словарь, 
# ключ - название страны, значение - список городов, 
# на вход поступает город, необходимо сказать из какой он страны


countries = {
    "Belarus": ["Minsk", "Brest", "Grodno"],
    "Russia": ["Moscow", "Saint Petersburg", "Kazan"],
    "Poland": ["Warsaw", "Krakow", "Gdansk"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
}

city = input()
for country, cities in countries.items():
    if city in cities:
        print(f'INFO: {city} is a city in {country}')
        break
else:
    print(f'ERROR: {city} not found')