import unittest
import main
import io
import unittest.mock
import numpy


class TestMain(unittest.TestCase):

    def setUp(self):
        self.station_reach = 13
        self.station_position = [5, 5]
        self.device_position = [15, 10]
        self.device_distance = main.calculate_station_distance(self.device_position, self.station_position)
        self.station_speed = main.calculate_station_speed(self.station_reach, self.device_distance)
        self.device_position_as_string = ','.join(map(str, self.device_position))
        self.station_position_as_string = ','.join(map(str, self.station_position))
        self.station_speed_formatted = round(self.station_speed, 1)
        self.best_station_string = f'Best network station for point ' \
                                   f'{self.device_position_as_string} is {self.station_position_as_string}' \
                                   f' with speed {self.station_speed_formatted}'
        self.no_station_found_string = f'No network station within reach for point {self.device_position_as_string}'

    def test_calculate_station_distance(self):
        self.assertTrue(type(self.station_position) is list)
        self.assertTrue(len(self.station_position) == 2)
        self.assertTrue(type(main.calculate_station_distance(self.device_position, self.station_position)) is numpy.float64)

    def test_calculate_station_speed(self):
        self.assertTrue(type(self.station_reach) is int)
        self.assertGreater(self.station_reach, 0)
        self.assertTrue(type(self.device_distance) is numpy.float64)
        self.assertEqual(main.calculate_station_speed(self.station_reach, self.device_distance), self.station_speed)

    def test_find_best_station(self):
        self.assertTrue(type(self.device_position) is list)
        self.assertTrue(len(self.device_position) == 2)
        best_station_speed, best_station_position = main.find_best_station(self.device_position)
        self.assertTrue(type(best_station_speed) is numpy.float64)
        self.assertTrue(type(best_station_position) is numpy.ndarray)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_friendly_print(self, mock_stdout):
        main.friendly_print(self.device_position, self.station_position, self.station_speed)
        self.assertIn(mock_stdout.getvalue().rstrip("\n"), {self.best_station_string, self.no_station_found_string})


if __name__ == '__main__':
    unittest.main()
