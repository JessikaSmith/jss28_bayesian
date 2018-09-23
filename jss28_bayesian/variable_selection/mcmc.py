__author__ = 'Maria Khodorchenko'
import numpy as np

class MCMC_Metropoolis:
    def __init__(self, x, func, step, thin=1):
        self.x = x
        self.func = func
        self.step = step
        self.thin = thin
        self.n_dims = self.x.size # if self.x.ndim == 1 else self.x.shape[1]

    def generator(self, num_sample, range=np.random):
        n_acc = 0
        l_trace = []
        acc_rate = []
        samples = np.empty([num_sample, self.n_dims])

        for n in range(num_sample):

            for _ in range(self.thin):
                s = self.x + self.step * np.random.randn(*self.x.shape)
                # r =