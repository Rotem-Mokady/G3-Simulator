from typing import Union
import numpy as np
# local modules
from config.constants import physical_constants


def get_piston_areas_ratio() -> Union[int, float]:
    """
    :return: Ratio between the up part area to the down part area of the piston.
    """
    return (
        np.square(physical_constants.Piston.RADIUS_METERS) -
        np.square(physical_constants.PushRod.RADIUS_METERS)
    ) / np.square(physical_constants.Piston.RADIUS_METERS)
