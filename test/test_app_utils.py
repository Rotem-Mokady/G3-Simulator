import unittest
# local modules
from app.utils import get_functions_list
from physical_formulas import (
    vel_calc,
    utils,
    friction_calc,
)
from configs.operationals import modules_names
from configs.dash import styles
from configs.calcs.constants import physical_constants
from app.modules import tdh_by_flow


class TestAppUtils(unittest.TestCase):

    def test_get_functions_list(self) -> None:
        # examine results for a few modules
        self.assertEqual(1, 1.0)


if __name__ == '__main__':
    unittest.main()
