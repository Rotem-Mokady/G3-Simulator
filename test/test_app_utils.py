import unittest
from typing import List
import os
from importlib import import_module
# local modules
from app.utils.extractions import get_functions_list
from calculations import (
    vel_calc,
    helpers,
    friction_calc,
)
from app.modules import tdh_by_flow
from configs.operationals import modules_names
from configs.dash import (
    styles,
    components,
    settings,
)
from configs.calcs.constants import physical_constants


class TestAppUtils(unittest.TestCase):

    def test_get_functions_list(self) -> None:

        # examine results for modules with functions
        good_inputs_to_results = {
            vel_calc: ['get_flow'],
            helpers: ['get_reynold_number', 'millimeters2meters', 'diameter2radius'],
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

    def test_components_modules(self) -> None:
        # make sure that in any module file has the relevant main method
        self.assertTrue(os.path.exists(components.COMPONENTS_CURRENT_DIR))
        # run on the configured dir path
        for file in os.listdir(components.COMPONENTS_CURRENT_DIR):
            # filter only relevant python files
            if file.endswith(settings.PY_FILE_EXTENSION) and file not in components.IRRELEVANT_FILES:

                filename_without_extension = file[:file.index(settings.PY_FILE_EXTENSION)]
                # current nodule
                curr_module = import_module(
                    "{current_dir}.{filename}".format(
                        current_dir=".".join(components.COMPONENTS_CURRENT_DIR.split("//")),
                        filename=filename_without_extension
                    )
                )
                # the checking itself
                self.assertIn(
                    components.MAIN_DASH_METHOD_PREFIX + filename_without_extension,
                    get_functions_list(curr_module)
                )

