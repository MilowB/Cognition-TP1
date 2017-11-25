import math

def curiosity(ite, itemax, sum_rew):
    if sum_rew == 0:
        sum_rew += 1
    stochas = (math.exp(-4 * float(ite) / float(itemax))) / abs(sum_rew)
    return stochas