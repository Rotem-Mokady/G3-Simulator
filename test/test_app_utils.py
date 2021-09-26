import unittest
from typing import List
# local modules
from app.utils import get_functions_list
from calculations import (
    vel_calc,
    utils,
    friction_calc,
)
from app.modules import tdh_by_flow
from configs.operationals import modules_names
from configs.dash import styles
from configs.calcs.constants import physical_constants


class TestAppUtils(unittest.TestCase):

    def test_get_functions_list(self) -> None:

        # examine results for modules with functions
        good_inputs_to_results = {
            vel_calc: ['get_flow'],
            utils: ['get_reynold_number', 'millimeters2meters', 'diameter2radius'],
            friction_calc: ['get_dynamic_friction_coefficient'],
            tdh_by_flow: ['calculate_tdh_by_flow', 'components_tdh_by_flow'],
        }
        for module, expected_results in good_inputs_to_results.items():
            results = get_functions_list(module)
            self.assertEqual(results, expected_results)
            self.assertIsInstance(results, List)

        # examine results for modules with no functions
        for module in [modules_names, styles, physical_constants]:
            self.assertEqual(get_functions_list(module), None)

        # examine wrong inputs
        for i in [12, "temp", lambda x: x + 1, ("a", "b")]:
            self.assertRaises(TypeError, get_functions_list, i)


if __name__ == '__main__':
    unittest.main()
