import math

def curiosity(ite, itemax, sum_rew):
    return (math.exp(-1 * float(ite) / float(itemax))) / sum_rew