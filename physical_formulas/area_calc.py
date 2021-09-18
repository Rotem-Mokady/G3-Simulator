from numbers import Number
import numpy as np
# local modules
from simulation_configs.calc_constants import physical_constants


def get_piston_areas_ratio() -> Number:
    """
    :return: Ratio between the up part area to the down part area of the piston.
    """
    return np.divide(
        np.subtract(
            np.square(physical_constants.Piston.RADIUS_METERS),
            np.square(physical_constants.PushRod.RADIUS_METERS)
        ),
        np.square(physical_constants.Piston.RADIUS_METERS)
    )
