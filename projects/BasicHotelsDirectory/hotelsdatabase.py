#citiesMap to prevent mistakes in spelling out the city when I do my HotelsDatabase.
citiesMap = dict(MIA='Miami', AUS='Austin', LA='Los Angeles', MIL='Milwaukee');

#Fake database of hotels.
HotelsDatabase = [
   {'_hotelID': 'aloft123', 'name': 'Aloft', 'city': citiesMap.get('AUS'), 'price per night': 79.99, 'ratings': [3.0, 2.5, 3.1], 'hasRestaurant': True},
   {'_hotelID': 'resid391', 'name': 'Residence Inn, Milwaukee', 'city': citiesMap.get('MIL'), 'price per night': 105.99, 'ratings': [3.0, 2.75, 2.5, 2.9], 'hasRestaurant': False},
   {'_hotelID': 'court591', 'name': 'Courtyard Austin', 'city': citiesMap.get('AUS'), 'price per night': 101.95, 'ratings': [3.75, 3.3, 2.5, 2.1, 2.9, 3.5], 'hasRestaurant': True},
   {'_hotelID': 'arch3191', 'name': 'Archer Hotel', 'city': citiesMap.get('AUS'), 'price per night': 57.99, 'ratings': [3.9, 4.0, 2.9, 3.0], 'hasRestaurant': False},
   {'_hotelID': 'mond97561', 'name': "Mondri'an", 'city': citiesMap.get("LA"), 'price per night': 133.99, 'ratings': [3.9, 3.5, 2.75, 4.0, 1.75, 1.9, 3.0], 'hasRestaurant': True},
   {'_hotelID': 'incmia315', 'name': 'Intercontinental Miami', 'city': citiesMap.get('MIA'), 'price per night': 53.99, 'ratings': [3.9, 3.75, 2.5], 'hasRestaurant': True},
   {'_hotelID': 'FAKE-HOTEL-1', 'name': 'Beer Garden Inn', 'city': citiesMap.get('MIL'), 'price per night': 19.99, 'ratings': [3.1, 1.5, 1.5, 3.3, 2.3, 3.0], 'hasRestaurant': False},
   {'_hotelID': 'mond87561', 'name': 'Ritz Carlton - Marina Del Rey', 'city': citiesMap.get("LA"), 'price per night': 201.99, 'ratings': [3.9, 3.9, 4.0, 2.1, 1.75, 3.3, 1.9, 4.0], 'hasRestaurant': True},
   {'_hotelID': 'ram11111', 'name': 'Ramada Windham', 'city': citiesMap.get('MIL'), 'price per night': 39.99, 'ratings': [3.5, 3.0, 2.75, 3.5, 3.1], 'hasRestaurant': True},
   {'_hotelID': '4ptSher979', 'name': 'Four Points Sheraton', 'city': citiesMap.get('MIA'), 'price per night': 99.35, 'ratings': [3.0, 2.5, 3.0, 3.0, 2.9], 'hasRestaurant': False},
   {'_hotelID': 'wholx519', 'name': 'W Hollywood', 'city': citiesMap.get('LA'), 'price per night': 73.99, 'ratings': [2.5, 3.9, 3.75, 3.0, 3.8, 3.6, 2.3, 3.1, 3.0], 'hasRestaurant': False}
]

#Sort hotels by city: {'los angeles': {...}, 'Austin': {...}, 'Miami': {...}}
def hotelsByCity(database):
   from functools import reduce;
   def CityDict(accumulator, val):
      city = val.get('city');
      _hotelID = val.get('_hotelID');
      if not accumulator.get(city): accumulator[city] = {f"{_hotelID}": {**val}};
      else: accumulator[city] = {**accumulator[city], f"{_hotelID}": {**val}};
      return accumulator;

   sortbycity = reduce(CityDict, database, {}); #final object.
   return sortbycity;