import unittest
from typing import List
import numpy as np
from datetime import datetime as dt
# local modules
from config.constants import physical_constants
from config.defaults import physical_deafult_params
from calculations.vel_calc import PipeVelocity
from calculations.area_calc import get_piston_areas_ratio
from calculations.utils import get_reynold_number
from calculations.friction_calc import get_dynamic_friction_coefficient
from calculations.height_calc import get_height_per_length


NUMBERS_TYPES = [int, float, np.int, np.int32, np.int64, np.float, np.float32, np.float64]


class TestCalc(unittest.TestCase):

    def test_pipe_velocities(self) -> None:

        # examine results for "down" input
        obj_1 = PipeVelocity("down")
        # make sure the basic attributes are fixed
        self.assertEqual(obj_1._movement_direction, "down")
        self.assertEqual(obj_1._piston_area_ratio, get_piston_areas_ratio())
        results_1 = obj_1.get_pipe_velocities()
        # final results should be in one list
        self.assertIsInstance(results_1, List)
        # make sure that there are only numbers in the list and all of them are equal or greater then zero
        for _ in results_1:
            self.assertIn(type(_), NUMBERS_TYPES)
            self.assertGreaterEqual(_, 0)

        # examine results for "up" input
        obj_2 = PipeVelocity("up")
        # make sure the basic attributes are fixed
        self.assertEqual(obj_2._movement_direction, "up")
        self.assertEqual(obj_2._piston_area_ratio, get_piston_areas_ratio())
        results_2 = obj_2.get_pipe_velocities()
        # final results should be in one list
        self.assertIsInstance(results_2, List)
        # make sure that there are only numbers in the list and all of them are equal or greater then zero
        for _ in results_2:
            self.assertIn(type(_), NUMBERS_TYPES)
            self.assertGreaterEqual(_, 0)

        # "down" and "up" should always be the same
        self.assertEqual(results_1, results_2)

        # any other value should raise a ValueError
        wrong_inputs = ["temp", 1, 2.2, {"a": ()}, dt.now()]
        for _ in wrong_inputs:
            self.assertRaises(ValueError, PipeVelocity(_).get_pipe_velocities)

    def test_piston_area_ratio(self) -> None:
        # get function results
        results = get_piston_areas_ratio()
        # calculate it with **2 instead of numpy.square built in function
        no_numpy_results = (
                                   physical_constants.Piston.RADIUS_METERS**2 -
                                   physical_constants.PushRod.RADIUS_METERS**2
                           ) / physical_constants.Piston.RADIUS_METERS**2
        self.assertEqual(results, no_numpy_results)
        self.assertIn(type(results), NUMBERS_TYPES)
        self.assertGreaterEqual(results, 0)

    def test_reynold_number(self) -> None:

        # define the different inputs
        good_diameter = 0.5
        bad_diameter = 'a'
        good_velocity = 4
        bad_velocity = [1, 2, 3]

        # make sure that we will get a TypeError if one argument or more is not fixed
        self.assertRaises(TypeError, get_reynold_number, bad_diameter, good_velocity)
        self.assertRaises(TypeError, get_reynold_number, good_diameter, bad_velocity)
        self.assertRaises(TypeError, get_reynold_number, bad_diameter, bad_velocity)
        # the results itself
        results = get_reynold_number(good_diameter, good_velocity)
        self.assertEqual(results, (good_diameter * good_velocity) / physical_constants.Water.NI)
        self.assertIn(type(results), NUMBERS_TYPES)
        self.assertGreaterEqual(results, 0)

    def test_dynamic_friction_coefficient(self) -> None:

        # define the different inputs
        good_diameter = 2
        bad_diameter = {'b'}
        good_velocity = 0.00000003
        bad_velocity = (50, ['c'], 70)
        good_pipe_types = list(physical_deafult_params.Pipe.TYPES_TO_E.keys())
        bad_pipe_types = ["Rotem", "Amit", "Ohad"]

        # make sure that we will get a TypeError if the diameter or the velocity are not fixed
        for pipe in good_pipe_types:
            self.assertRaises(TypeError, get_dynamic_friction_coefficient, bad_diameter, good_velocity, pipe)
            self.assertRaises(TypeError, get_dynamic_friction_coefficient, good_diameter, bad_velocity, pipe)
            self.assertRaises(TypeError, get_dynamic_friction_coefficient, bad_diameter, bad_velocity, pipe)

        # make sure that we will get a value error if the pipe are not exist
        for pipe in bad_pipe_types:
            self.assertRaises(ValueError, get_dynamic_friction_coefficient, good_diameter, good_velocity, pipe)

        # make sure that the output is in the right type for all the relevant pipe types
        for pipe in good_pipe_types:
            results = get_dynamic_friction_coefficient(good_diameter, good_velocity, pipe)
            self.assertIn(type(results), NUMBERS_TYPES)
            self.assertGreaterEqual(results, 0)

    def test_get_height_per_length(self) -> None:
        # define the different inputs
        good_diameter = 0.05549523
        bad_diameter = {'b': 12}
        good_velocity = 100000
        bad_velocity = [-1, dt.utcnow(), dt.now()]
        good_pipe_types = list(physical_deafult_params.Pipe.TYPES_TO_E.keys())
        bad_pipe_types = [1, 2, 4]

        # make sure that we will get a TypeError if the diameter or the velocity are not fixed
        for pipe in good_pipe_types:
            self.assertRaises(TypeError, get_height_per_length, bad_diameter, good_velocity, pipe)
            self.assertRaises(TypeError, get_height_per_length, good_diameter, bad_velocity, pipe)
            self.assertRaises(TypeError, get_height_per_length, bad_diameter, bad_velocity, pipe)

        # make sure that we will get a value error if the pipe are not exist
        for pipe in bad_pipe_types:
            self.assertRaises(ValueError, get_height_per_length, good_diameter, good_velocity, pipe)

        # make sure that the output is in the right type for all the relevant pipe types, and the calculate is right
        for pipe in good_pipe_types:
            results = get_height_per_length(good_diameter, good_velocity, pipe)

            self.assertIn(type(results), NUMBERS_TYPES)
            self.assertGreaterEqual(results, 0)
            self.assertAlmostEqual(
                results,
                get_dynamic_friction_coefficient(
                    diameter=good_diameter,
                    velocity=good_velocity,
                    pipe_type=pipe
                ) / 2 / physical_constants.Earth.GRAVITY * np.square(good_velocity) / good_diameter
            )


if __name__ == '__main__':
    unittest.main()




