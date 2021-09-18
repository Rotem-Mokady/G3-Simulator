from numbers import Number
import pandas as pd
from copy import deepcopy
# local modules
from simulation_configs.calc_constants import physical_constants
from simulation_configs.calc_constants.default_varibles import physical_deafult_params
from simulation_configs.operational_constants.tables import TDHbyFlowNames
from physical_formulas.vel_calc import (
    PipeVelocity,
    get_flow,
)
from physical_formulas.resistence_calc import get_tdh
from physical_formulas.utils import (
    diameter2radius,
    millimeters2meters,
)


def get_tdh_by_flow(
        height_meters: Number,
        pipe_diameter_millimeters: Number,
        pipe_type: str
) -> pd.DataFrame:
    """
    :param height_meters: integer. The distance between the machine and the ground.
    :param pipe_diameter_millimeters: integer. Pipe's diameter in millimeters.
    :param pipe_type: str. Pipe's type.
    :return: DataFrame. The Pipe's TDH scale for every Piston's flow
    """
    # Piston basic facts
    piston_velocities = deepcopy(physical_deafult_params.Piston.CURRENT_DOWN_VELOCITIES)
    piston_radius_meters = physical_constants.Piston.RADIUS_METERS
    # Flow calculation
    piston_flows = list(
        map(lambda vel: get_flow(
            radius=piston_radius_meters,
            velocity=vel
        ), piston_velocities)
    )

    # convert pipe's diameter from millimeters to meters
    pipe_diameter_meters = millimeters2meters(pipe_diameter_millimeters)
    # convert pipe's diameter to radius
    pipe_radius_meters = diameter2radius(pipe_diameter_meters)
    # pipe's velocities as a results of the chosen radius
    pipe_velocities = PipeVelocity(pipe_radius=pipe_radius_meters).get_pipe_velocities()
    # TDH calculation
    pipe_tdh = list(
        map(lambda vel: get_tdh(
            height=height_meters,
            diameter=pipe_diameter_meters,
            velocity=vel,
            pipe_type=pipe_type
        ), pipe_velocities)
    )

    # create a DataFrame of the results
    df = pd.DataFrame()
    df[TDHbyFlowNames.FLOW_COLUMN_NAME] = pd.Series(piston_flows)
    df[TDHbyFlowNames.TDH_COLUMN_NAME] = pd.Series(pipe_tdh)
    return df
