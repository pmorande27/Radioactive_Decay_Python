import numpy as np
import random as r


class isotope(object):
    def __init__(self, dimension, decay_constant, time_step):
        self.dimension = dimension
        self.decay_constant = decay_constant
        self.time_step = time_step
        self.nuclei = np.ones((self.dimension, self.dimension))
        self.initial_nuclei = dimension * dimension
        self.alive = dimension * dimension
        self.historicalIsotope = [self.nuclei.copy()]

    def decay(self):
        t = 0
        while self.alive > (self.initial_nuclei / 2):
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.nuclei[i][j] = self.decide_decay(self.nuclei[i][j])
            self.historicalIsotope += [self.nuclei.copy()]
            t += self.time_step
        print(t)

    def decide_decay(self, number):
        if number == 1:
            if r.random() < self.decay_constant * self.time_step:
                self.alive -= 1
                return 0
            else:
                return 1
        else:
            return 0
