import numpy as np


# loc, scale
def generate_from_normal(num, **kwargs):
    return np.random.normal(size=num, scale=kwargs.get('scale', 1))


def generate_from_uniform():
    raise NotImplementedError


class RegressionModel:
    def __init__(self, **kwargs):
        self.datax = generate_from_normal(kwargs.get('shape', 1), scale=10)  # n x k
        self.datay = generate_from_normal(kwargs.get('shape', 1)[0])  # n x k
        #self.datay  =

    # params of distribution should be passed
    def simulate_data(self, beta_num, beta_distrib='normal', error='normal', **kwargs):
        assert beta_distrib in ['normal', 'uniform']
        assert error in ['normal', 'uniform']

        raise NotImplementedError
