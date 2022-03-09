from scipy.spatial import distance
import numpy


stations = numpy.array([
    [0, 0, 9],
    [20, 20, 6],
    [10, 0, 12],
    [5, 5, 13],
    [99, 25, 2],
])
devices = numpy.array([[0, 0],
                    [100, 100],
                    [15, 10],
                    [18, 18],
                    [13, 13],
                    [25, 99]])


def calculate_station_distance(a, b):
    return distance.euclidean(a, b)


def calculate_station_speed(reach, station_distance):
    speed = (reach - station_distance) ** 2
    if station_distance > reach:
        speed = 0
    return speed


def find_best_station(device_position):
    best_station_speed = 0
    best_station_position = []
    for station in stations:
        station_position = station[:2]
        station_reach = station[-1]
        station_distance = calculate_station_distance(station_position, device_position)
        station_speed = calculate_station_speed(station_reach, station_distance)
        if station_speed > best_station_speed:
            best_station_speed = station_speed
            best_station_position = station_position
    return best_station_speed, best_station_position
