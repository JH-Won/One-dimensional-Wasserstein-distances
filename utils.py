from numpy import log
from scipy.special import betaln
from scipy.special import comb
import numpy as np


def sample_poisson_process(rate=0.5, window_size=100):
    """
    Realize Poisson point process of a given rate in window size.
    """
    scale = rate ** (-1)
    number_points = np.random.poisson(window_size / scale)
    points = np.random.uniform(low=0, high=window_size, size=number_points)
    points.sort()
    return points


def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):   # python 3
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
    
    
def binomln(n, k):
    "Log of scipy.special.binom calculated entirely in the log domain"
    return -betaln(1 + n - k, 1 + k) - log(n + 1)


def exp_was_dist(n, m, lambda1, lambda2, scale=False):
    """
    Derived distance between n- and m-th spikes from two Poisson processes of rates lambda1 and lambda2
    """
    
    assert n >= 1
    assert m >= 1
    
    val1 = 0
    log_pstr1 = np.log(lambda1) - np.log(lambda1 + lambda2)
    log_pstr2 = np.log(lambda2) - np.log(lambda1 + lambda2)
    for k in range((n + m) + 1):
        val1 += np.exp(binomln(n + m, k) + k*log_pstr1 + (n + m - k)*log_pstr2)*np.abs(n - k)
    val_test7 = val1*(1/lambda1 + 1/lambda2)
    
    if not scale:
        return val_test7
    else:
        return val1

