# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:59:30 2020

@author: AWalker8
"""
import numpy as np
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
        
        self.action_space = gym.spaces.Discrete(3)
        
        '''
        the available pricing actions are
        1 = -10
        2 = 0
        3 = +10
        '''
        #observation_high = np.array([100,1000,20])
        #observation_low = np.array([20,0,0])
        
        self.observation_space = spaces.Tuple((
        spaces.Discrete(9),
        spaces.Discrete(200),
        spaces.Discrete(20)))
        
        
        #self.observation_space = spaces.Discrete(observation_low, observation_high,dtype=np.float32, shape=(9,1000,20))
        
        
        #Price
        pr = 50
        # tickets left
        tl = 200
        # days till gig
        ds = 20
          
        self.state = [pr,tl,ds]
        self.reward = 0
        self.done = False
        
        # Also retain the price history and sales for reviewing how effective it is
        self.history = {'price':[self.state[0]],
                        'tickets_left':[self.state[1]],
                        'days_remaining':[self.state[2]],
                        'tickets_sold': [0],
                        'reward':[self.reward]
                        }
        
        return None
    
    
      
    def step(self, action):
      
        '''
        update the environment based on the action taken
        In this version only options are to increase price by +10, 0, or - 10,
        once a week. 
    
        '''
        action_options = [-10,0,10]
        actual_action = action_options[action]

    #Change the price to reflect the action taken.
        # Put limits on the price. 
        # Can't have price less than 15.
        if ((self.state[0] + actual_action )>= 20 ) and ((self.state[0] + actual_action) <= 100 ): 
            self.state[0] =  self.state[0] + actual_action
        elif (self.state[0] + actual_action < 20 ) :
            self.state[0] = 20
        else:
            self.state[0] = 100
        
        # Use new price to simulate how many tickets are sold. Create function to imitate demand. 
        # This function needs to be replaced with the most accurate representation of reality.
        sales = int(10* 0.985**(self.state[0]) * (1/(0.985**self.state[2])))
        
        # update the remaining tickets left and revenue. Check how many seats are actually left.
        # Can't sell more tickets than are available. 
        if self.state[1] < sales:
            # Case when there are more sales than available tickets
            # here sell all available. 
            self.reward = self.reward + (self.state[1] * self.state[0])
            self.history['tickets_sold'].append(self.state[1])
            self.state[1] = 0
        else:
            self.state[1] = self.state[1] - sales
            self.history['tickets_sold'].append(sales)
            # For now, make reward the sales * price. (Basic revenue)
            self.reward = self.reward + (sales * self.state[0])
       
        #update the remaining days left
        self.state[2] = self.state[2] - 1
        
        if self.state[2] == 0:
            self.done = True
            
        self.history['price'].append(self.state[0])
        self.history['tickets_left'].append(self.state[1])
        self.history['reward'].append(self.reward)
        self.history['days_remaining'].append(self.state[2])
        
        
        return [self.state, self.reward, self.done, self.history]
      
    def reset(self):
        pr = 50
        tl = 200
        ds = 20
                  
        self.state = [pr,tl,ds]
        self.reward = 0
        self.done = False
        self.history = {'price':[self.state[0]],
                        'tickets_left':[self.state[1]],
                        'days_remaining':[self.state[2]],
                        'tickets_sold': [0],
                        'reward':[self.reward]
                        }
          
        return self.state
    
    def render(self, mode='human', close=False):
        return None
      