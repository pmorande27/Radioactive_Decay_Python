import numpy as np
import random as r
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from matplotlib import patches

def createNewIsotope (dimension):
        row = [ 1 for i in range (0, dimension)]
        array2D = [row for i in range (0, dimension)]
        return array2D

class decay(object):
    def __init__(self, dimension, decay_constant, time_step):
        self.dimension = dimension
        self.decay_constant = decay_constant
        self.time_step = time_step
        self.nuclei = np.ones((self.dimension, self.dimension))
        self.initial_nuclei = dimension * dimension
        self.historicalIsotope = [self.nuclei.copy()]

    def decay(self):
        alive = self.initial_nuclei
        t = 0
        while alive > (self.initial_nuclei / 2):
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if self.nuclei[i][j] == 1:
                        if r.random() < self.decay_constant * self.time_step:
                            self.nuclei[i][j] = 0
                            alive -= 1
                        else:
                            continue
            self.historicalIsotope += [self.nuclei.copy()]
            t += self.time_step
        
        print(t)

    def animateDecay (self):
        fig = plt.figure()
        images = []
        for array2D in self.historicalIsotope:
            plt.title("Isotope Decay: ", fontsize = 16)
            renderImage = plt.pcolor(array2D, cmap = colors.ListedColormap (["Red", "Green"]), edgecolors='k', linewidth = 2, animated = True)
            images.append([renderImage]) 
        ani = animation.ArtistAnimation(fig, images, interval = 0.01, blit = True,repeat=False)
        plt.show()

    def displayIsotope (self):
        plt.axis('off')
        plt.title("Isotope Decay: ", fontsize = 16)
        redLabel = patches.Patch(color='red', label='Decayed nuclei')
        greenLabel = patches.Patch(color='green', label='Undecayed nuclei')
        plt.legend(handles=[redLabel,greenLabel])
        plt.pcolor(self.nuclei, cmap = colors.ListedColormap (["Red", "Green"]), edgecolors='k', linewidth = 2)
        plt.show()


def main():
    d = decay(10, 0.02775,0.01)
    d.decay()
    d.animateDecay()
    d.displayIsotope()

main()
