import numpy as np

def generate_from_normal(num, **kwargs):
    raise NotImplementedError

def generate_from_uniform():
    raise NotImplementedError

class RegressionModel():
    def __init__(self):
        beta = {}
        error = {}

    # params of distribution should be passed
    def simulate_data(self, beta_num, beta_distrib='normal', error='normal', **kwargs):
        assert beta_distrib in ['normal', 'uniform']
        assert error in ['normal', 'uniform']

        raise NotImplementedError