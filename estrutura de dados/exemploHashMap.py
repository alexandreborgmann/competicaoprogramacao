from collections import defaultdict

city_map = defaultdict(list)
print(city_map)

cities = ['Calgary', 'Vancouver', 'Toronto']
city_map['Canada'] += cities
print(city_map)
print(city_map['Canada'][1])

cities = ['Sao Paulo', 'Rio de Janeiro', 'Porto Alegre']
city_map['Brasil'] += cities
city_list = city_map.values()
print(city_list)