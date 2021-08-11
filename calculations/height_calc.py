from typing import Union
import numpy as np
# local modules
from config.constants.physical_constants import Earth
from calculations.friction_calc import get_dynamic_friction_coefficient


def get_height_per_length(
        diameter: Union[int, float],
        velocity: Union[int, float],
        pipe_type: str
) -> Union[int, float]:
    """
    :param diameter: Int or float. Pipe's diameter.
    :param velocity: Int or float. Pipe's velocity.
    :param pipe_type: str. Pipe's type for getting the relevant F parameter.
    :return: Int or float. Height's delta per length for specific pipe situation.
    """
    f = get_dynamic_friction_coefficient(
        diameter=diameter,
        velocity=velocity,
        pipe_type=pipe_type
    )
    g = 1 / (2 * Earth.GRAVITY)
    v_d = np.square(velocity) / diameter
    return f * g * v_d
