from numbers import Number
from typing import (
    Union,
    Dict,
)
import pandas as pd
from copy import deepcopy
from dash import Dash
from dash.dependencies import (
    Input,
    Output,
)
import plotly.graph_objects as go
# local modules
from configs.calcs.constants import physical_constants
from configs.calcs.defaults import physical_deafult_params
from configs.operationals.tables import TDHbyFlowNames
from formulas.vel_calc import (
    PipeVelocity,
    get_flow,
)
from formulas.resistence_calc import get_tdh
from formulas.utils import (
    diameter2radius,
    millimeters2meters,
)
from configs.dash import (
    properties,
    styles,
    main_dropdown,
    modules_constants,
)
from configs.operationals import modules_names


def calculate_tdh_by_flow(
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


def components_tdh_by_flow(app: Dash) -> None:
    """
    :param app: The main Dash object of the site.
    The function adds a few components that calculates the TDH by flow.
    :return: The server object itself.
    """
    @app.callback(
        Output(component_id=modules_constants.TDHbyFlow.ID, component_property=properties.STYLE_PROPERTY),
        [Input(component_id=main_dropdown.ID, component_property=main_dropdown.PROPERTY)]
    )
    def show(value: str) -> Dict:
        if value == modules_names.TDH_BY_FLOW:
            return styles.BUTTONS_STYLE
        else:
            return styles.HIDE_STYLE

    @app.callback(
        Output(component_id=modules_constants.TDHbyFlow.ActivateButton.ID, component_property=properties.STYLE_PROPERTY),
        [Input(component_id=modules_constants.TDHbyFlow.Pipe.ID, component_property=properties.VALUE_PROPERTY),
         Input(component_id=modules_constants.TDHbyFlow.Diameter.ID, component_property=properties.VALUE_PROPERTY),
         Input(component_id=modules_constants.TDHbyFlow.PipeType.ID, component_property=properties.VALUE_PROPERTY)]
    )
    def activate(pipe: Union[str, Number], diameter: Union[str, Number], pipe_type: str) -> Dict:
        if (
            pipe == modules_constants.TDHbyFlow.Pipe.AUTO_COMPLETE or
            diameter == modules_constants.TDHbyFlow.Diameter.AUTO_COMPLETE or
            pipe_type == modules_constants.TDHbyFlow.PipeType.AUTO_COMPLETE or
            None in [pipe, diameter, pipe_type]
        ):
            return styles.HIDE_STYLE
        else:
            return styles.ACTIVATION_BUTTONS_STYLE

    @app.callback(
        Output(component_id=modules_constants.TDHbyFlow.Graph.ID, component_property=properties.FIG_PROPERTY),
        Output(component_id=modules_constants.TDHbyFlow.Graph.ID, component_property=properties.STYLE_PROPERTY),
        [Input(component_id=modules_constants.TDHbyFlow.ActivateButton.ID, component_property=properties.CLICK_PROPERTY)]
    )
    def calc(n_clicks: Number):
        return None, styles.HIDE_STYLE
        # if not n_clicks:
        #     return None, styles.HIDE_STYLE
