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

city = "Minsk"

country = list(filter(lambda x:city in countries[x], countries))

print(country)