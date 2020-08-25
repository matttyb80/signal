from src.sim.model.parts.marketing_signal import *
from src.sim.model.parts.adoption import *

partial_state_update_block = [
    {
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # PUBLIC MILESTONE SIGNAL
        'policies': {
            'marketing_rate': p_marketing_rate,
            'p_marketing_shock' : p_marketing_shock,
        },
        'variables': {
            'public_alpha': s_signal,
            'milestone_progress': s_granular_progress,
            'expected_milestone_interpolation': s_expected_milestone_interpolation,
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