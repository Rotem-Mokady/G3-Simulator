from numbers import Number
import numpy as np
# local modules
from physical_formulas.height_calc import get_height_per_length


def get_tdh(
        height: Number,
        diameter: Number,
        velocity: Number,
        pipe_type: str
) -> Number:
    """
    :param height: integer. Pipe's distance from the ground.
    :param diameter: integer. Pipe's diameter.
    :param velocity: integer. Pipe's velocity.
    :param pipe_type: str. Pipe's type for getting the relevant height per length number.
    :return: integer. The TDH scale.
    """
    if not isinstance(height, Number):
        raise TypeError("height should be integer")
    height_per_length = get_height_per_length(
        diameter=diameter,
        velocity=velocity,
        pipe_type=pipe_type
    )
    return np.add(
        height,
        np.multiply(
            height_per_length,
            height
        )
    )
