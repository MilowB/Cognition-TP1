import math

def curiosity(ite, itemax, sum_rew):
    if sum_rew == 0:
        sum_rew += 1
    return (math.exp(-1 * float(ite) / float(itemax))) / sum_rew