from geopy.distance import great_circle
from aiogram import types
from utils.misc import show_on_gmaps
from data.locations import Shops


def calc_distance_geopy(lat1, lon1, lat2, lon2):
    """ Рассчитывает расстояние между двумя точками """

    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    return great_circle(coords_1, coords_2).km


def choose_shortest(location: types.Location, max_n=3):
    """Выбирает ближайшие точки """

    distances = list()
    for shop_name, shop_location in Shops:
        distances.append((shop_name,
                          calc_distance_geopy(location.latitude, location.longitude,
                                              shop_location["lat"], shop_location["lon"]),
                          show_on_gmaps.show(**shop_location),
                          shop_location
                          ))
    return sorted(distances, key = lambda x: x[1])[:max_n]
