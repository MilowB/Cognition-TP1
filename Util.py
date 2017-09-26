import math

def curiosity(ite, itemax, sum_rew):
    l0 = 0.10
    return (l0 * math.exp(-1 * float(ite) / float(itemax))) / sum_rew