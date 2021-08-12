from typing import Union
import numpy as np
import math
# local modules
from config.defaults import physical_deafult_params
from calculations.utils import get_reynold_number


def get_dynamic_friction_coefficient(
        diameter: Union[int, float],
        velocity: Union[int, float],
        pipe_type: str
) -> Union[int, float]:
    """
    :param diameter: Int or float. Pipe's diameter.
    :param velocity: Int or float. Pipe's velocity.
    :param pipe_type: str. Pipe's type for getting the relevant E parameter.
     Type that is not exist will raise an error.
    :return: Int or float. The friction coefficient.
    """
    try:
        e = physical_deafult_params.Pipe.TYPES_TO_E[pipe_type]
    except KeyError:
        raise ValueError(f"Type {pipe_type} is not an option for pipe")

    reynold_number = get_reynold_number(
        diameter=diameter,
        velocity=velocity
    )
    left_side = e / diameter / 3.7
    right_side = 5.74 / np.power(reynold_number, 0.9)

    return 0.25 / np.square(
        math.log10(
             left_side + right_side
        )
    )
