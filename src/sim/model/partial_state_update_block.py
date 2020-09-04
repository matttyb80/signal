from src.sim.model.parts.progress_signal import *
from src.sim.model.parts.adoption import *

partial_state_update_block = [
    {
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # PUBLIC MILESTONE SIGNAL
        'policies': {
            'milestone_rate': p_milestone_rate,
            'p_milestone_shock' : p_milestone_shock,
        },
        'variables': {
            'public_alpha': s_signal,
            'milestone_progress': s_granular_progress,
            'expected_milestone_linear': s_expected_milestone_linear,
            'expected_milestone_step': s_expected_milestone_step,
            'expected_milestone_quad': s_expected_milestone_quad,
        }
    },
    {
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Private signal update
        'policies': {

        },
        'variables': {
            'milestone_difference_signal': s_milestone_difference_signal,           # SUB POPULATION BASED

        }
    },

]