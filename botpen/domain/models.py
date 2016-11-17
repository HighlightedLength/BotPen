from collections import namedtuple
from enum import Enum

Agent = namedtuple('Agent',
    [   "id",

        "x",
        "y",
        "theta",

        "actuation_noise_x",
        "actuation_noise_y",
        "actuation_noise_theta",

        "observation_noise_x",
        "observation_noise_y",
        "observation_noise_theta",

        "behavior_type",
        "behavior_config"])

ParametricBehavior = namedtuple('ParametricBehavior',
    [   'time',
        'x',
        'y',
        'theta'])

Control = namedtuple('Control', 'x y theta')

Move = namedtuple('Move',
    [   'id',
        'expected_dx',
        'noise_dx',
        'actual_dx',
        'x',

        'expected_dy',
        'noise_dy',
        'actual_dy',
        'y',

        'expected_dtheta',
        'noise_dtheta',
        'actual_dtheta',
        'theta'])

Observation = namedtuple('Observation',
    [   'odometries',
        'ranges',
        'base_agent'])

Odometry = namedtuple('Odometry',
    [   'noise_dx',
        'dx',
        'noise_dy',
        'dy',
        'noise_dtheta',
        'dtheta'])

Range = namedtuple('Range',
    [   'dx',
        'dy',
        'dtheta'])

class Procedure(Enum):
    finish = 0
    pause = 1
    step = 2
    auto = 3

Lifecycle = namedtuple('Lifecycle',
    [   'finish',
        'proceed'])

Estimation = namedtuple('Estimation',
    [   'agent_id',
        'x',
        'y',
        'theta'])
