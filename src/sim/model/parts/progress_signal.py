# import networkx as nx
import numpy as np

# from ..utils import *

def p_milestone_rate(params, substep, state_history, prev_state, **kwargs):
    # params = params[0]
    """
    Policy for steady marketing spend signal generation.
    """
    constant = params['CLAIMS_MAGNITUDE']
    random = np.random.normal(params['CLAIMS_MAGNITUDE'], scale = params['CLAIMS_STD'])
    return {'granular_progress': random}

def p_milestone_shock(params, substep, state_history, prev_state, **kwargs):
    """
    Policy for shock marketing (spend and other sources).
    """
    # Expected number of shocks
    # coded through parameter
    # params = params[0]
    freq = params['MILESTONE_FREQUENCY'] * 0.5

    # expected but randomized through poisson
    if np.random.poisson(freq) > params['MILESTONE_FREQUENCY']:
        shock = params['MILESTONE_MAGNITUDE']
    else:
        shock = 0
    return {'milestone_signal': shock}

def s_signal(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'public_alpha'

    value = policy_input['milestone_signal']
    return (key, value)


def s_granular_progress(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'milestone_progress'

    prev_value = prev_state['milestone_progress']
    value = prev_value  + policy_input['granular_progress']
    return (key, value)


def s_expected_milestone_linear(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'expected_milestone_linear'

    prev_value = prev_state['expected_milestone_linear']
    
    new_value = params['CLAIMS_MAGNITUDE']

    value = prev_value + new_value
    return (key, value)

def s_expected_milestone_step(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'expected_milestone_step'

    time = prev_state['timestep']
    
    df = prev_state['milestone']


    value = df.loc[df['Completion_Time'] <= time]['Completion_Percent'].values[-1]

    return (key, value)

def s_expected_milestone_quad(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'expected_milestone_quad'

    time = prev_state['timestep']
    
    df = prev_state['milestone']

    increment = params['CLAIMS_MAGNITUDE']
    prev_value = prev_state['expected_milestone_quad']

    y_one = df.loc[df['Completion_Time'] <= time]['Completion_Percent'].values[-1]
    x_one = df.loc[df['Completion_Time'] <= time]['Completion_Time'].values[-1]
  

    y_two = df.loc[df['Completion_Time'] > time]['Completion_Percent'].values[0]
    x_two = df.loc[df['Completion_Time'] > time]['Completion_Time'].values[0]
    # Piecewise quadratic derviative
    # a =  ( y_2/ x^2_2)
    # y-prime = 2 * ( y_2/ x^2_2) * (time - time_1)
    
    a = (y_two - y_one) / ((x_two - x_one)**2)


    
    # derivative =
    value = prev_value + 2 * a *(time - x_one)

    return (key, value)

def s_milestone_difference_signal(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'milestone_difference_signal'

    expected = prev_state['expected_milestone_linear']
    
    actual  =  prev_state['milestone_progress']


    value = actual -  expected
    return (key, value)