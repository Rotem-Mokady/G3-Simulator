from numbers import Number
import numpy as np
# local modules
from config.constants.physical_constants import Earth
from physical_formulas.friction_calc import get_dynamic_friction_coefficient


def get_height_per_length(
        diameter: Number,
        velocity: Number,
        pipe_type: str
) -> Number:
    """
    :param diameter: integer. Pipe's diameter.
    :param velocity: integer. Pipe's velocity.
    :param pipe_type: str. Pipe's type for getting the relevant F parameter.
    :return: integer. Height's delta per length for specific pipe situation.
    """
    f = get_dynamic_friction_coefficient(
        diameter=diameter,
        velocity=velocity,
        pipe_type=pipe_type
    )
    g = np.divide(
        1,
        np.multiply(
            2,
            Earth.GRAVITY
        )
    )
    v_d = np.divide(
        np.square(velocity),
        diameter
    )
    return np.multiply(
        np.multiply(
            f,
            g
        )
        , v_d
    )
