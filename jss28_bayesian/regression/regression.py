import numpy as np


# loc, scale
def generate_from_normal(num, **kwargs):
    return np.random.normal(size=num, scale=kwargs.get('scale', 1))


def generate_from_uniform():
    raise NotImplementedError


class RegressionModel:
    def __init__(self, **kwargs):
        self.datax = generate_from_normal(kwargs.get('shape', 1), scale=10)  # n x k
        self.datay = self.generate_outcome(kwargs.get('shape', 1)[0])
        # self.datay  =

    # TODO: introduce
    def generate_outcome(self, size):
        np.random.seed(42)
        alpha = 5
        beta = generate_from_normal(size, scale=2).reshape((100, 1))
        res = alpha + np.sum(beta * self.datax, axis=1).reshape((100, 1)) + np.random.randn(size).reshape((100, 1))
        self.datay = res

    # params of distribution should be passed
    def simulate_data(self, beta_num, beta_distrib='normal', error='normal', **kwargs):
        assert beta_distrib in ['normal', 'uniform']
        assert error in ['normal', 'uniform']

        raise NotImplementedError
