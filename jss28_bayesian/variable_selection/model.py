__author__ = 'Maria Khodorchenko'

import pymc3 as pm
import numpy as np
import multiprocessing
import theano.tensor as tt


class Model:
    def __init__(self):
        self.model = None
        self.trace = None

    def loglikelihood_t(self, x):
        return -1.5 * tt.log(1 - x ** 2)

    def loglikelihood_s(self, x):
        return -tt.log(np.abs(x))

    def createModel(self, xdata, ydata=None):
        shape = xdata.shape
        with pm.Model() as model:
            alpha = pm.Normal('alpha', mu=0, sd=100)
            theta = pm.DensityDist('theta', self.loglikelihood_t, shape=30, testval=0)
            sigma = pm.DensityDist('sigma', self.loglikelihood_s, testval=1)
            e = pm.Normal('e', mu=0, sd=1)
            _sum = theta[0] * xdata[:, 0].T
            for i in range(1, shape[1]):
                _sum += theta[i] * xdata[:, i].T
            likelihood = pm.Normal('estimated', mu=alpha + _sum + e,
                                   sd=sigma, shape=100)  # observed=ydata
            trace = pm.sample(2000, cores=multiprocessing.cpu_count())
        self.trace = [trace['alpha'], trace['theta'], trace['sigma'], trace['e']]
