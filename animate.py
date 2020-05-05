
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from matplotlib import patches
from Radioactive_Decay_Python.Isotope import isotope


class animate(object):
    def __init__(self, dimension, decay_constant, time_step):
        self.isotope = isotope(dimension, decay_constant, time_step)
        self.isotope.decay()

    def animateDecay(self):
        fig = plt.figure()
        images = []
        for array2D in self.isotope.historicalIsotope:
            plt.title("Isotope Decay: ", fontsize=16)
            renderImage = plt.pcolor(array2D, cmap=colors.ListedColormap(["Red", "Green"]), edgecolors='k', linewidth=2,
                                     animated=True)
            images.append([renderImage])
        ani = animation.ArtistAnimation(fig, images, interval=0.01, blit=True, repeat=False)
        plt.show()

    def displayIsotope(self):
        plt.axis('off')
        plt.title("Isotope Decay: ", fontsize=16)
        redLabel = patches.Patch(color='red', label='Decayed nuclei')
        greenLabel = patches.Patch(color='green', label='Undecayed nuclei')
        plt.legend(handles=[redLabel, greenLabel])
        plt.pcolor(self.isotope.nuclei, cmap=colors.ListedColormap(["Red", "Green"]), edgecolors='k', linewidth=2)
        plt.show()
