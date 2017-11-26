import math

def curiosity(ite, itemax, sum_rew):
    if sum_rew == 0:
        sum_rew += 1
    stochas = (math.exp(-4 * float(ite) / float(itemax))) / abs(sum_rew)
    return stochas

def curiosity(ite, itemax):
    stochas = (math.exp(-4 * float(ite) / float(itemax)))
    return stochas

def rescale(value, min , max, interval):
    oldRange = (max - min) #15
    newRange = (interval[1] - interval[0]) #1
    #newValue = (((value - interval[0]) * newRange) / oldRange) + min #
    newValue = (((value - min) * (interval[1] - interval[0])) / (max - min)) + interval[0]
    return newValue