from typing import Union
# local modules
from config.constants import physical_constants


def get_reynold_number(
        diameter: Union[int, float],
        velocity: Union[int, float]
) -> Union[int, float]:
    """
    :param diameter: Int or float. Pipe's diameter.
    :param velocity: Int or float. Pipe's velocity.
    :return: Int or float. The reynold number.
    """
    return (diameter * velocity) / physical_constants.Water.NI



