import math

'''
Objectif :
Permet de dire si une recompense est significativement differente de celles recues habituellement.
'''
class Student:
    def __init__(self, samples):
        #Echantillons que sur lesquels il y aura comparaison
        self.samples = samples

    def isSignificant(self, data):
        #Calcule de l'estimateur non biaise de la variance (represente par "s" ici)
        n = 4
        average = 0
        for samp in self.samples:
            average += samp
        average /= len(self.samples)
        s = float(1) / float(n - 1)
        somme = 0
        for samp in self.samples:
            somme += float(math.pow(samp - average, 2))
        s += somme
        #Calcule du quantile a n degre de liberte
        t = self.tvalue(average, data, s, n)
        #Dans la t table, pour un degre de liberte de 4, la valeur critique est 2.776 (alpha = 5%)
        #Si t > 2.776 alors la difference est significative
        if abs(t) > 2.776:
            return True
        else:
            return False

    def tvalue(self, average, data, s, n):
        return float(average - data) / float(s / math.sqrt(n))
