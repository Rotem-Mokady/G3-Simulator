from numbers import Number
import numpy as np
# local modules
from configs.calcs.constants import physical_constants


def get_reynold_number(
        diameter: Number,
        velocity: Number
) -> Number:
    """
    :param diameter: integer. Pipe's diameter.
    :param velocity: integer. Pipe's velocity.
    :return: integer. The reynold number.
    """
    if not isinstance(diameter, Number):
        raise TypeError("diameter should be an integer")
    if not isinstance(velocity, Number):
        raise TypeError("velocity should be an integer")
    return np.divide(
        np.multiply(
            diameter,
            velocity
        ),
        physical_constants.Water.NI
    )


def millimeters2meters(
        number_in_millimeters: Number
) -> Number:
    """
    The function converts from millimeters to meters.
    :param number_in_millimeters: integer.
    :return: The number with dividing by one thousand.
    """
    if not isinstance(number_in_millimeters, Number):
        raise TypeError("input should be an integer")
    return np.divide(number_in_millimeters, 1000)


def diameter2radius(
        diameter: Number
) -> Number:
    """
    The function converts from diameter to radius.
    :param diameter: integer.
    :return: The number with dividing by two.
    """
    if not isinstance(diameter, Number):
        raise TypeError("input should be an integer")
    return np.divide(diameter, 2)

