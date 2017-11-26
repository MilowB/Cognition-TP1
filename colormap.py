from pylab import *
import math

class ColorMap():
    def __init__(self, data):
        self._data = data

    def build(self):
        transformed = self.sort_(self._data, int(math.sqrt(len(self._data))))
        #(i, min, max) Interpolation de couleurs selon i entre les bornes min et max pour r, g et b
        cdict = {'red': ((0.0, 0.4, 0.7),
                        (1.0, 0.0, 0.0)),
                'green': ((0.0, 0.0, 0.0),
                        (1.0, 0.7, 1.0)),
                'blue': ((0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0))}
        my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
        pcolor(transformed, cmap=my_cmap)

        unite = str(int(math.sqrt(len(self._data))))
        legend = "Temps : 1 unité = " + unite + " itérations"
        title("Récompenses au fil du temps")
        xlabel(legend)
        ylabel("Temps :  1 unité = 1 itération")

        cbar = colorbar()
        cbar.ax.set_ylabel("Récompense après action")

        savefig("Images/colormaps.png",dpi=100,facecolor='gray')

    '''
    Objectif : Compte le nombre d'elements dans un tableau de tableau
    '''
    def nb_elements(self, data):
        nb = 0
        for d in data:
            for axiom in d:
                nb += 1
        return nb

    '''
    Objectif : Trie selon modulo
    '''
    def sort_(self, data, heigth):
        ret = []
        cpy_data = list(data)
        cpt = 0
        while self.nb_elements(ret) < len(cpy_data) - 5000:
            new_arr = []
            for i in range(len(cpy_data)):
                if i % heigth == 0:
                    if i + cpt <= len(cpy_data) - 1:
                        new_arr.append(cpy_data[i + cpt])
                    else:
                        break
            cpt += 1
            ret.append(new_arr)
        return ret


