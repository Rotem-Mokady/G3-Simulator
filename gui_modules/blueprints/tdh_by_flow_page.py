import streamlit as st
from typing import Union, Dict
from numbers import Number
import numpy as np
# local modules
from operational_calculations.tdh_by_flow import get_tdh_by_flow
from simulation_configs.streamlit_website import settings


def pipe_height_input() -> Union[Number, Dict]:
    """
    :return: pipe height user input.
    """
    pipe_height = st.number_input(
        label=settings.TDHbyFlow.PIPE_HEIGHT_INPUT_BUTTON_NAME,
        min_value=settings.TDHbyFlow.PIPE_HEIGHT_INPUT_MIN_VALUE
    )
    if pipe_height:
        if not isinstance(pipe_height, Number) or np.less(pipe_height, settings.TDHbyFlow.PIPE_HEIGHT_INPUT_MIN_VALUE):
            st.error(settings.TDHbyFlow.PIPE_HEIGHT_INPUT_WRONG_MESSAGE.format(user_input=pipe_height))
            return settings.Inputs.BAD_RESPONSE
        st.info(settings.TDHbyFlow.PIPE_HEIGHT_INPUT_GOOD_MESSAGE.format(user_input=pipe_height))
        return pipe_height
    return settings.Inputs.BAD_RESPONSE


def pipe_diameter_input() -> Union[Number, Dict]:
    """
    :return: pipe diameter user input.
    """
    pipe_diameter = st.number_input(
        label=settings.TDHbyFlow.PIPE_DIAMETER_INPUT_BUTTON_NAME,
        min_value=settings.TDHbyFlow.PIPE_DIAMETER_INPUT_MIN_VALUE
    )
    if pipe_diameter:
        if not isinstance(pipe_diameter, Number) or np.less(pipe_diameter, settings.TDHbyFlow.PIPE_DIAMETER_INPUT_MIN_VALUE):
            st.error(settings.TDHbyFlow.PIPE_DIAMETER_INPUT_WRONG_MESSAGE.format(user_input=pipe_diameter))
            return settings.Inputs.BAD_RESPONSE
        st.info(settings.TDHbyFlow.PIPE_DIAMETER_INPUT_GOOD_MESSAGE.format(user_input=pipe_diameter))
        return pipe_diameter
    return settings.Inputs.BAD_RESPONSE


def tdh_by_flow_blueprint() -> None:
    """
    GUI simulation TDH by Flow function when there is a pressing on the relevant button.
    """
    if st.button("temp1"):
        pipe_height = pipe_height_input()
        if pipe_height:
            st.balloons()
    if st.button("temp2"):
        pipe_diameter = pipe_diameter_input()
        if pipe_diameter:
            st.balloons()
    # if not pipe_height:
    #     st.experimental_rerun()
    # pipe_diameter = pipe_diameter_input()
    # st.write(pipe_height)
    # st.write(pipe_diameter)
    # if pipe_height:
    #     pipe_diameter = pipe_diameter_input()
    # elif pipe_diameter:
    #     pipe_height = pipe_height_input()

