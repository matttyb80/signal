from datetime import datetime
# import networkx as nx
import numpy as np
import pandas as pd

# from copy import deepcopy
# import scipy.stats as stats
# from .sys_params import sys_params
from src.sim.model.utils import *
from src.sim.sim_setup import SIMULATION_TIME_STEPS, MONTE_CARLO_RUNS
# Initial Values
signal = 0
# state = 0
adoption = Adoption()
# pool = Adoption_Pool() # Iniialized in config loop using source_pool parameter

MILESTONES = [0, 1,2,3,4]
milestone_df = pd.DataFrame(MILESTONES, columns = ['Name'])
milestone_df['Completion_Time'] =  SIMULATION_TIME_STEPS * milestone_df.Name // (max(MILESTONES))
milestone_df['Completion_Percent'] = 100 * milestone_df.Name // (max(MILESTONES) )


## Genesis States #################################################
genesis_states = {
    'timestamp': datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
    'public_alpha': signal,
    'milestone' : milestone_df,
    'milestone_progress' : 0, 
    # 'adoption': adoption,  # Agent Based
    # 'pool' : pool,  # Iniialized in config loop using source_pool parameter

}