from typing import List, Union
from numbers import Number
import numpy as np
from copy import deepcopy
# local modules
from configs.calcs.constants import math_constants, physical_constants
from configs.calcs.defaults import physical_deafult_params
from formulas.area_calc import get_piston_areas_ratio


class PipeVelocity:

    def __init__(
            self,
            movement_direction: str = "down",
            pipe_radius: Number = physical_constants.Pipe.RADIUS_METERS,
    ) -> None:
        """
        Define a few relevant variables.
        """
        self._movement_direction = movement_direction
        self._pipe_radius = pipe_radius
        self._piston_area_ratio = get_piston_areas_ratio()  # calculation of Piston's areas ratio
        self._multiple_param = None

    def get_pipe_velocities(self) -> List[Number]:
        """
        The main method of the class.
        :return: List.
            Pipe's current velocities.
        """
        current_velocities = self._current_velocities
        return self._get_pipe_velocities(current_velocities)

    @property
    def _current_velocities(self) -> List:
        """
        The function create the relevant multiple parameter based on the chosen movement direction.
        Raises an error in case of wrong direction input which is not exist.
        :return: List.
            Piston's current velocities as a results of the chosen movement direction.
        """
        if self._movement_direction == "down":
            self._multiple_param = self._down_multiple_param
            results = physical_deafult_params.Piston.CURRENT_DOWN_VELOCITIES
        elif self._movement_direction == "up":
            self._multiple_param = self._up_multiple_param
            results = self._get_piston_up_velocities()
        else:
            raise ValueError(f"No movement direction named {self._movement_direction}")

        assert self._multiple_param and isinstance(self._multiple_param, (int, float))
        return results

    @property
    def _down_multiple_param(self) -> Number:
        """
        :return: integer.
            Piston's down multiple parameter.
        """
        return deepcopy(self._piston_area_ratio)

    @property
    def _up_multiple_param(self) -> Number:
        """
        :return: integer.
            Piston's up multiple parameter.
        """
        return 1

    def _get_piston_up_velocities(self) -> List[Number]:
        """
        :return: List.
            Piston's current up velocities.
        """
        return list(
            map(
                self._get_piston_up_velocity,
                physical_deafult_params.Piston.CURRENT_DOWN_VELOCITIES
            )
        )

    def _get_piston_up_velocity(
            self,
            current_piston_down_velocity: Number
    ) -> Number:
        """
        :param current_piston_down_velocity: integer. Current piston down velocity.
        :return: integer.
            Piston's current up velocity.
        """
        return np.multiply(
            self._piston_area_ratio,
            current_piston_down_velocity
        )

    def _get_pipe_velocities(
            self,
            current_piston_velocities: List[Number]
    ) -> List[Number]:
        """
        :param current_piston_velocities: list. Current piston velocities.
        :return: list.
            Pipe's current velocities as a results of the current piston velocities.
        """
        return list(map(self._get_pipe_velocity, current_piston_velocities))

    def _get_pipe_velocity(
            self,
            current_piston_velocity: Number
    ) -> Number:
        """
        :param current_piston_velocity: integer. Current piston velocity.
        :return: integer.
            Pipe's current velocity.
        """
        return np.multiply(
            np.multiply(
                self._multiple_param,
                current_piston_velocity
            ),
            np.square(
                np.divide(
                    physical_constants.Piston.RADIUS_METERS,
                    self._pipe_radius_checker
                )
            )
        )

    @property
    def _pipe_radius_checker(self) -> Union[Number, None]:
        try:
            assert isinstance(self._pipe_radius, Number)
        except AssertionError:
            raise ValueError("Radius pipe must be an integer")
        return self._pipe_radius


def get_flow(
    radius: Number,
    velocity: Number
) -> Number:
    """
    :param radius: integer. Piston's radius.
    :param velocity: integer. Piston's velocity.
    :return: integer. The full energy.
    """
    if not isinstance(radius, Number):
        raise TypeError("radius should be integer")
    if not isinstance(velocity, Number):
        raise TypeError("velocity should be integer")
    return np.multiply(
        math_constants.PI,
        np.multiply(
            np.square(radius),
            velocity
        )
    )
