__author__ = 'Maria Khodorchenko'

import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
import matplotlib

def plot_params(N_SAMPLES, alpha_samples, theta_samples):
    plt.subplot(211)
    plt.title(r"""Distribution of $\alpha$ with %d samples""" % N_SAMPLES)

    plt.hist(alpha_samples, histtype='stepfilled',
             color='darkred', bins=30, alpha=0.8, density=True)
    plt.ylabel('Probability Density')

    plt.subplot(212)
    plt.title(r"""Distribution of $\theta$ with %d samples""" % N_SAMPLES)
    plt.hist(theta_samples, histtype='stepfilled',
             color='darkblue', bins=30, alpha=0.8, density=True)
    plt.ylabel('Probability Density')
    plt.show()


def plot_trace(alpha_samples, theta_samples):
    # Plot alpha trace
    plt.subplot(211)
    plt.title(r'Trace of $\alpha$')
    plt.plot(alpha_samples, color = 'darkred')
    plt.xlabel('Samples'); plt.ylabel('Parameter')

    # Plot beta trace
    plt.subplot(212)
    plt.title(r'Trace of $\beta$')
    plt.plot(theta_samples, color='b')
    plt.xlabel('Samples'); plt.ylabel('Parameter')
    plt.tight_layout(h_pad=0.8)
    plt.show()