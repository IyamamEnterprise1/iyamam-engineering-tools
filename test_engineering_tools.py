import math
import unittest
from engineering_tools import (convert, circular_area, rectangular_area,
                               velocity, air_changes_per_hour)


class EngineeringTests(unittest.TestCase):
    def test_known_unit_values(self):
        self.assertAlmostEqual(convert(1, "ft", "mm"), 304.8)
        self.assertAlmostEqual(convert(1, "cfm", "L/s"), .4719474432)
        self.assertAlmostEqual(convert(3600, "m3/h", "m3/s"), 1)
        self.assertAlmostEqual(convert(1, "bar", "kPa"), 100)

    def test_temperatures(self):
        self.assertAlmostEqual(convert(32, "F", "C"), 0)
        self.assertAlmostEqual(convert(100, "C", "F"), 212)
        self.assertAlmostEqual(convert(0, "K", "C"), -273.15)

    def test_geometry_and_flow(self):
        self.assertAlmostEqual(circular_area(2), math.pi)
        self.assertAlmostEqual(rectangular_area(.4, .5), .2)
        self.assertAlmostEqual(velocity(1, .2), 5)
        self.assertAlmostEqual(air_changes_per_hour(.5, 300), 6)
        self.assertEqual(velocity(0, .2), 0)

    def test_invalid_inputs(self):
        cases = [(convert, (1, "m", "Pa")), (convert, (1, "unknown", "m")),
                 (convert, (-1, "K", "C")), (convert, (math.inf, "m", "ft")),
                 (circular_area, (0,)), (rectangular_area, (-1, 2)),
                 (velocity, (-1, 1)), (velocity, (1, 0)),
                 (air_changes_per_hour, (1, math.nan))]
        for function, arguments in cases:
            with self.subTest(function=function.__name__, arguments=arguments):
                with self.assertRaises(ValueError):
                    function(*arguments)


if __name__ == "__main__":
    unittest.main()
