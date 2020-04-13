# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:59:30 2020

@author: AWalker8
"""

import gym
from gym import error, spaces, utils
from gym.utils import seeding

class gigticketEnv(gym.Env):
  
    metadata = {'render.modes': ['human']}
    '''
      Class that defines the environment used to train the agent.
      The environment simulates the environment for the gig ticket problem.
      
      In this problem, the state will include 
      pr - price of the ticket
      tl - number of tickets left
      rd - reward - which will be a function of revenue
      ds - days till gig
      [pr,tl,rd,ds]
      
      For a gym environment 4 methods are required. init, step, reset and render. 
      
      '''
    
    def __init__(self):
      
        ''' 
        Initialise the environment at the beginning of one pass through the environment.
        For now simple version that has one starting price £50 one capacity 1000,
        one lead time 5 days and initial reward 0. 
        '''
          
        pr = 50
        tl = 1000
        rd = 0
        ds = 5
          
        self.state = [pr,tl,rd,ds]
        self.reward = 0
        self.done = 0
        self.add_info = 0
        return None
      
    def step(self, action):
      
        '''
        update the environment based on the action taken
        In this version only options are to increase price by +10, 0, or - 10,
        once a week. 
        '''
      
        self.state[0] =  self.state[0] + action
      
      # How may tickets were sold. Create function to imitate demand. 
      #sales = 
      
     
        return [self.state, self.reward, self.done, self.add_info]
      
    def reset(self):
        pr = 50
        tl = 1000
        rd = 0
        ds = 5
                  
        self.state = [pr,tl,rd,ds]
        self.reward = 0
        self.done = 0
        self.add_info = 0
          
        return self.state
    
    def render(self, mode='human', close=False):
        return None
      