import unittest
import pandas as pd
from numbers import Number
# local modules
from configs.calcs.defaults import physical_deafult_params
from configs.operationals.tables import TDHbyFlowNames
from app.tdh_by_flow import get_tdh_by_flow


class TestCalc(unittest.TestCase):

    def test_tdh_by_flow(self) -> None:

        # define the different inputs
        good_height = 0.7
        bad_height = [0.6]
        good_diameter = 2
        bad_diameter = "T"
        good_pipe_types = list(physical_deafult_params.Pipe.TYPES_TO_E.keys())
        bad_pipe_types = ["a", "b", "c"]

        # make sure that we will get a TypeError if the height or the diameter are not fixed
        for pipe in good_pipe_types:
            self.assertRaises(TypeError, get_tdh_by_flow, bad_height, good_diameter, pipe)
            self.assertRaises(TypeError, get_tdh_by_flow, good_height, bad_diameter, pipe)
            self.assertRaises(TypeError, get_tdh_by_flow, bad_height, bad_diameter, pipe)

        # make sure that we will get a value error if the pipe is not exist
        for pipe in bad_pipe_types:
            self.assertRaises(ValueError, get_tdh_by_flow, good_height, good_diameter, pipe)

        # make sure that the output is in the right format
        for pipe in good_pipe_types:
            # the results itself
            results = get_tdh_by_flow(good_height, good_diameter, pipe)
            # correct types
            self.assertIsInstance(results, pd.DataFrame)
            for _ in results[TDHbyFlowNames.FLOW_COLUMN_NAME]:
                self.assertIsInstance(_, Number)
            for _ in results[TDHbyFlowNames.TDH_COLUMN_NAME]:
                self.assertIsInstance(_, Number)
            # correct columns
            self.assertCountEqual(
                results.columns.tolist(),
                [
                    TDHbyFlowNames.FLOW_COLUMN_NAME,
                    TDHbyFlowNames.TDH_COLUMN_NAME
                ])
            # correct size
            self.assertEqual(
                len(physical_deafult_params.Piston.CURRENT_DOWN_VELOCITIES),
                len(results)
            )


if __name__ == '__main__':
    unittest.main()
