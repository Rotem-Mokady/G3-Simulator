from numbers import Number
import numpy as np
import math
# local modules
from config.defaults import physical_deafult_params
from physical_formulas.utils import get_reynold_number


def get_dynamic_friction_coefficient(
        diameter: Number,
        velocity: Number,
        pipe_type: str
) -> float:
    """
    :param diameter: integer. Pipe's diameter.
    :param velocity: integer. Pipe's velocity.
    :param pipe_type: str. Pipe's type for getting the relevant E parameter.
     Type that is not exist will raise an error.
    :return: integer. The friction coefficient.
    """
    try:
        e = physical_deafult_params.Pipe.TYPES_TO_E[pipe_type]
    except KeyError:
        raise ValueError(f"Type {pipe_type} is not an option for pipe")

    reynold_number = get_reynold_number(
        diameter=diameter,
        velocity=velocity
    )
    left_side = np.divide(
        np.divide(
            e,
            diameter
        ),
        3.7
    )
    right_side = np.divide(
        5.74,
        np.power(reynold_number, 0.9)
    )

    return np.divide(
        0.25,
        np.square(
            math.log10(
                np.add(
                    left_side,
                    right_side
                )
            )
        )
    )
