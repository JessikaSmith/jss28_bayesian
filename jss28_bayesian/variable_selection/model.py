__author__ = 'Maria Khodorchenko'

import pymc3 as pm
import numpy as np
import multiprocessing
import theano.tensor as tt
from theano.compile import mode
from scipy import stats
import matplotlib.pyplot as plt

import theano


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
            e = pm.Normal('e', mu=0, sd=1, shape=100)
            _sum = theta[0] * xdata[:, 0]
            for i in range(1, shape[1]):
                _sum += theta[i] * xdata[:, i]
            print(_sum)
            likelihood = pm.Normal('estimated', mu=(alpha + _sum + e).astype('float32'),
                                   sd=sigma.astype('float32'), shape=100, observed=ydata)
            step = pm.Metropolis()
            trace = pm.sample(200) #cores=multiprocessing.cpu_count())
        self.trace = [trace['alpha'], trace['theta'], trace['sigma'], trace['e']]

    def testModel(self):
        n = 100
        heads = 61
        a, b = 10, 10
        prior = stats.beta(a, b)
        post = stats.beta(heads+a, n-heads+b)
        ci = post.interval(0.95)

        xs = np.linspace(0, 1, 100)

        niter = 2000
        with pm.Model() as coin_context:
            p = pm.Beta('p', alpha=2, beta=2)
            y = pm.Binomial('y', n=n, p=p, observed=heads)
            start = pm.find_MAP()
            step = pm.Metropolis()
            trace = pm.sample(niter, step=step, start=start, njobs=1, random_seed=123)
