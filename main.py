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
