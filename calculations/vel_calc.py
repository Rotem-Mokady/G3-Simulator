from typing import List, Union
import numpy as np
from copy import deepcopy
# local modules
from config.constants import (
    physical_constants,
)
from config.defaults import physical_deafult_params
from calculations.area_calc import get_piston_areas_ratio


class PipeVelocity:

    def __init__(
            self,
            movement_direction: str = "down"
    ) -> None:
        """
        Define a few relevant variables.
        """
        self._movement_direction = movement_direction
        self._piston_area_ratio = get_piston_areas_ratio()  # calculation of Piston's areas ratio
        self._multiple_param = None

    def get_pipe_velocities(self) -> Union[List[int], List[float]]:
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
    def _down_multiple_param(self) -> Union[int, float]:
        """
        :return: Int or float.
            Piston's down multiple parameter.
        """
        return deepcopy(self._piston_area_ratio)

    @property
    def _up_multiple_param(self) -> Union[int, float]:
        """
        :return: Int or float.
            Piston's up multiple parameter.
        """
        return 1

    def _get_piston_up_velocities(self) -> Union[List[int], List[float]]:
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
            current_piston_down_velocity: Union[int, float]
    ) -> Union[int, float]:
        """
        :param current_piston_down_velocity: int or float. Current piston down velocity.
        :return: Int or float.
            Piston's current up velocity.
        """
        return self._piston_area_ratio * current_piston_down_velocity

    def _get_pipe_velocities(
            self,
            current_piston_velocities: Union[List[int], List[float]]
    ) -> Union[List[int], List[float]]:
        """
        :param current_piston_velocities: list. Current piston velocities.
        :return: List.
            Pipe's current velocities as a results of the current piston velocities.
        """
        return list(map(self._get_pipe_velocity, current_piston_velocities))

    def _get_pipe_velocity(
            self,
            current_piston_velocity: Union[int, float]
    ) -> Union[int, float]:
        """
        :param current_piston_velocity: int or float. Current piston velocity.
        :return: Int or float.
            Pipe's current velocity.
        """
        return self._multiple_param * current_piston_velocity * np.square(
            physical_constants.Piston.RADIUS_METERS /
            physical_constants.Pipe.RADIUS_METERS
        )

