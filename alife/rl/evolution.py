from numpy import *
from agent import Agent

class Evolver(Agent):
    '''
        Evolver.

        Uses a random weight matrix.
        Relies entirely on generation-to-generation evolution to make any progress as a species.
    '''

    def __init__(self, S, A):
        """
            Init.


            Parameters
            ----------

            S : BugSpace
                observation space
            A : BugSpace
                action space

        """
        self.S = S
        self.A = A
        D = S.shape[0]
        L = A.shape[0]
        # Set random weights.
        self.W = random.randn(D,L) * (random.rand(D,L) >= 0.5)     # weights
        self.w = random.randn(L) * 0.1                             # bias

    def act(self,x,r,done=False):
        """
            Act.

            Parameters
            ----------

            x : numpy array of length D
                the state at the current time
            r : float
                the reward signal at the current time

            Returns
            -------

            A number array of length L 
                (the action to take)
        """

        # No learning, just a simple reflex.
        a = dot(x,self.W) + self.w
        return a

    def spawn(self):
        """
            Spawn.

            Returns
            -------
            
            A new copy (child) of this agent, [optionally] based on this one (the parent).
        """
        b = Evolver(self.S,self.A)
        # Make a random adjustment to the weight matrix.
        L = self.A.shape[0]
        b.W = (self.W + random.randn(*self.W.shape) * 0.1) * (self.W > 0.0)
        b.w = b.w + random.randn(L) * 0.01
        return b

