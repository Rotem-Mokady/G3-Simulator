from typing import Union
# local modules
from calculations.height_calc import get_height_per_length


def get_tdh(
        height: Union[int, float],
        diameter: Union[int, float],
        velocity: Union[int, float],
        pipe_type: str
) -> Union[int, float]:
    """
    :param height: Int or float. Pipe's distance from the ground.
    :param diameter: Int or float. Pipe's diameter.
    :param velocity: Int or float. Pipe's velocity.
    :param pipe_type: str. Pipe's type for getting the relevant height per length number.
    :return: Int or float. The TDH scale.
    """
    height_per_length = get_height_per_length(
        diameter=diameter,
        velocity=velocity,
        pipe_type=pipe_type
    )
    return height + height_per_length * height
