# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:58:58 2020

@author: AWalker8
"""

from gym.envs.registration import register

register(
    id='gigticket-v0',
    entry_point='gym_gigticket.envs:gigticketEnv',
)