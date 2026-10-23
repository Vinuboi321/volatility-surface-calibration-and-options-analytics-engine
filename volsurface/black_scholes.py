"""Black-Scholes pricing for European calls and puts."""

import numpy as np
from scipy.stats import norm


def d1_d2(S, K, T, r, q, sigma):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2


def bs_price(S, K, T, r, q, sigma, is_call=True):
    d1, d2 = d1_d2(S, K, T, r, q, sigma)
    stock_part = S * np.exp(-q * T)
    strike_part = K * np.exp(-r * T)
    if is_call:
        return stock_part * norm.cdf(d1) - strike_part * norm.cdf(d2)
    return strike_part * norm.cdf(-d2) - stock_part * norm.cdf(-d1)