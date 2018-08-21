__author__ = 'Maria Khodorchenko'
import numpy as np


class MCMC_Metropoolis:
    def __init__(self, x, func, step, thin=1):
        self.x = x
        self.func = func
        self.step = step
        self.thin = thin

    def generator(self, num_sample, range=np.random):
        n_acc = 0
        l_trace = []
        acc_rate = []
        samples = np.empty

        for _ in range():
