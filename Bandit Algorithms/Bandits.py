'''
-----------------------------------------
Bandits Algorithm: Explore then Commit
                   Upper Confidence Bound
-----------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt
import random

n = 10000 # horizon
k = 100 # number of experiments
####### Explore then Commit ######

# probability arrays for arms

# problem 1
probabs_1 = np.array([0.6, 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3])

# problem 2
probabs_2 = np.array([0.62, 0.6, 0.6, 0.6, 0.6, 0.58, 0.58, 0.58, 0.5, 0.5])

# problem 3
probabs_3 = np.array([0.8, 0.4, 0.3, 0.2, 0.1])

# problem 4
probabs_4 = np.array([1/20, 1/16, 1/12])

def explore(arms,m,n,prob='binomial'):
    '''
    explore in Explore then Commit
    arms: mean of arms
    m: number of times to pull each arm
    n: horizon length
    '''
    pull_arr = []
    regret_arr = []
    optimal_arm = np.max(arms)
    pull_counter=np.zeros(len(arms))
    arm_reward_arr = [] # array to store the reward for each arm
    regret = 0
    for i in range(len(arms)):
        arm_reward = 0
        for pull_no in range(m):
            mean = arms[i] # mean of the arm
            if prob == 'binomial':
                reward = np.random.binomial(1,mean,1)[0] # sample with bernoulli probab:mean
                pull_counter[i]+=1
                pull_arr.append(i)
            if prob == 'uniform':
                reward = 1
                pull_counter[i]+=1
                pull_arr.append(i)
            arm_reward+=reward
            delta = optimal_arm - arms[i]  # get the gap
            regret+= delta
            regret_arr.append(regret)
        arm_reward_arr.append(arm_reward)
        
    return arm_reward_arr,regret,pull_counter,regret_arr,pull_arr


def commit(arms,arm_reward_arr,m,n,regret,pull_counter,regret_arr,pull_arr,prob='binomial'):
    '''
    commit in Explore then Commit
    arms: mean of arms
    m: number of times to pull each arm
    n: horizon length
    '''
    total_iter = n - m*len(arms) # n - mK
    highest_arm_index = np.argmax(arm_reward_arr)
    optimal_arm = np.max(arms) # u*
    max_mean = np.max(arm_reward_arr)
    for i in range(total_iter):
        if prob == 'binomial':
            reward = np.random.binomial(1,arms[highest_arm_index],1)[0]
            pull_counter[highest_arm_index]+=1
            pull_arr.append(highest_arm_index)
        if prob == 'uniform':
            reward = 1
            pull_counter[highest_arm_index]+=1
            pull_arr.append(highest_arm_index)
        regret+= optimal_arm - arms[highest_arm_index]
        regret_arr.append(regret)
    return regret,pull_counter,pull_arr,regret_arr


def ETC(arms,m,n,k):
    '''
    Explore then Commit
    arms: mean of arms
    m: number of times to pull each arm
    n: horizon length
    k: number of experiments
    '''
    regret_exp = []
    pull_exp = []
    for experiment in range(k):
        arm_reward_arr,regret,pull_counter,regret_arr,pull_arr=explore(arms,m,n)
        regret,pull_counter,pull_arr,regret_arr = commit(arms,arm_reward_arr,m,n,regret,pull_counter,regret_arr,pull_arr)
        regret_exp.append(regret_arr)
        pull_exp.append(pull_arr)
        
    return regret_exp,pull_exp
        
m_arr = [1,20,100,200,500]
color = ['r','g','b','y','k']
for i in range(len(m_arr)):
    r,p=ETC(probabs_1,m_arr[i],n,k)
    mean_regret = np.mean(r,axis=0)
    x = np.linspace(0,n,len(mean_regret))
    plt.plot(x, mean_regret, color[i],label='m='+str(m_arr[i]))
    # plt.fill_between(x, mean_regret-mean_std/2, mean_regret+mean_std/2,color=color[i],alpha=1.4)
    plt.grid()
    plt.legend()
plt.show()


