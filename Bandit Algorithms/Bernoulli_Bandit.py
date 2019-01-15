import numpy as np
import matplotlib.pyplot as plt


class BernoulliBandit:
    # accepts a list of K >= 2 floats , each lying in [0 ,1]
    def __init__ (self,means):
        self.means = means
        self.action_count = np.zeros(len(self.means))
    # Function should return the number of arms
    def K(self):
        return len(self.means)
        
    # Accepts a parameter 0 <= a <= K -1 and returns the
    # realisation of random variable X with P(X = 1) being
    # the mean of the (a+1) th arm.
    def pull (self,a):
        mean=self.means[a] # set the mean of the bernoulli probability
        return np.random.binomial(1,mean,1) # pull the arm
# Returns the regret incurred so far.
    def regret(self):
        

def Greedy (bandit , n) :
# implement the Follow -the - Leader algorithm by replacing
# the code below that just plays the first arm in every round
    for t in range (n) :
        bandit.pull(0)
        

class ActionSpace(object):
    def __init__(self, actions):
        self.actions = actions
        self.n = len(actions)
        
### BanditEnv Environment
 
class BanditEnv(Environment):
 
    def __init__(self, num_actions = 10, distribution = "bernoulli", evaluation_seed="387"):
        super(BanditEnv, self).__init__()
        self.action_space = ActionSpace(range(num_actions))  # get the mean of all arms
        self.distribution = distribution  # get the probability distribution type
 
        np.random.seed(evaluation_seed)
 
        self.reward_parameters = None
        if distribution == "bernoulli":
            self.reward_parameters = np.random.rand(num_actions) # probab distro on arms
        elif distribution == "normal":
            self.reward_parameters = (np.random.randn(num_actions),np.random.rand(num_actions))
        else:
            print("Please use a supported reward distribution") #, flush = True)
            sys.exit(0)
 
        # selection of optimal arm
        if distribution != "normal":
            self.optimal_arm = np.argmax(self.reward_parameters) # take max of all arms
        else:
            self.optimal_arm = np.argmax(self.reward_parameters[0])
 
 
    def compute_gap(self, action):
        if self.distribution != "normal":
            gap = np.absolute(self.reward_parameters[self.optimal_arm]- self.reward_parameters[action])
        else:
            gap = np.absolute(self.reward_parameters[0][self.optimal_arm] - self.reward_parameters[0][action])
        return gap
 
    def step(self, action):
        self.is_reset = False
 
        valid_action = True
        if (action is None or action = self.action_space.n):
            print("Algorithm chose an invalid action; reset reward to -inf")#, flush = True)
            reward = float("-inf")
            gap = float("inf")
            valid_action = False
 
        if self.distribution == "bernoulli":
            if valid_action:
                reward = np.random.binomial(1, self.reward_parameters[action])
                gap = self.reward_parameters[self.optimal_arm] -self.reward_parameters[action]
        elif self.distribution == "normal":
            if valid_action:
                reward = self.reward_parameters[0][action] + self.reward_parameters[1][action] * np.random.randn()
                gap = self.reward_parameters[0][self.optimal_arm] - self.reward_parameters[0][action]

        else:
            print("Please use a supported reward distribution")#, flush = True)
            sys.exit(0)
 
    return(None, reward, self.is_reset, '')
 
#Policy interface
class Policy:
#num_actions: (int) Number of arms [indexed by 0 ... num_actions-1]
    def __init__(self, num_actions):
        self.num_actions = num_actions
 
    def act(self):
        pass
 
def feedback(self, action, reward):
pass


