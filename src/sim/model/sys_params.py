# import networkx as nx
from pprint import pprint

import numpy as np
import itertools

### CLAIMS PARAMETERS #################################
# noisy uniform distribution of claims signalling
# parameters for magnitude, frequency, and variance
CLAIMS_MAGNITUDE = [10] # tablet use, function of activity + adoption
CLAIMS_FREQUENCY = [1]  # 1 =daily
CLAIMS_STD = [0.5, 1, 2]

# Milestone event signalling magnitude and expected frequency
# large scale and low frequency
MILESTONE_MAGNITUDE = [100]
MILESTONE_FREQUENCY = [10]

### EXTERNAL EXPERIENCE PARAMETERS #################################
# If UX/UI are not part of the model. Can use as an external signal to
#  generate stochastic process for experience.
EXO_EXPERIENCE = [140]

### POPULATION POOL PARAMETERS #################################
SOURCE_POOL = [100000] #, 12]

### INITIAL THRESHOLD VALUE PARAMETERS #################################
MILESTONE_THRESHOLD = [0.8]
LEAK_COEFFICIENT = [0.01]


#### USE ONLY FOR A/B WITH PARAMETER SWEEPS OR MULTIPLE PARAMETER SWEEPS #####

factors = [CLAIMS_MAGNITUDE, CLAIMS_FREQUENCY, CLAIMS_STD, MILESTONE_MAGNITUDE, MILESTONE_FREQUENCY, MILESTONE_THRESHOLD]
product = list(itertools.product(*factors))
CLAIMS_MAGNITUDE,CLAIMS_FREQUENCY, CLAIMS_STD, MILESTONE_MAGNITUDE, MILESTONE_FREQUENCY, MILESTONE_THRESHOLD = zip(*product)
CLAIMS_MAGNITUDE = list(CLAIMS_MAGNITUDE)
CLAIMS_FREQUENCY = list(CLAIMS_FREQUENCY)
CLAIMS_STD = list(CLAIMS_STD)
MILESTONE_MAGNITUDE = list(MILESTONE_MAGNITUDE)
MILESTONE_FREQUENCY = list(MILESTONE_FREQUENCY)
MILESTONE_THRESHOLD = list(MILESTONE_THRESHOLD)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
sys_params = {
   'CLAIMS_MAGNITUDE': CLAIMS_MAGNITUDE,
   'CLAIMS_FREQUENCY': CLAIMS_FREQUENCY, 
   'CLAIMS_STD': CLAIMS_STD,
   'MILESTONE_MAGNITUDE': MILESTONE_MAGNITUDE,
   'MILESTONE_FREQUENCY': MILESTONE_FREQUENCY,
   'MILESTONE_THRESHOLD': MILESTONE_THRESHOLD,
}