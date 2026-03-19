import numpy as np
from im_engine.sensitivities.delta import compute_delta_sensitivity
from im_engine.sensitivities.bucket import assign_bucket
from im_engine.aggregation.correlation import get_correlation

def compute_initial_margin(portfolio):
    sensitivities = []

    for trade in portfolio.get_trades():
        sens = compute_delta_sensitivity(trade)
        bucket = assign_bucket(trade)
        sensitivities.append((sens, bucket))

    im = 0.0

    for i in range(len(sensitivities)):
        s_i, b_i = sensitivities[i]
        for j in range(len(sensitivities)):
            s_j, b_j = sensitivities[j]
            rho = get_correlation(b_i, b_j)
            im += s_i * s_j * rho

    return np.sqrt(im)