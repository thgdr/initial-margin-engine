import numpy as np

def compute_delta_sensitivity(trade):
    # Simplified proxy for sensitivity
    # In reality: derivative of price wrt risk factor

    if trade.asset_class == "Rates":
        return 0.01 * trade.notional * np.exp(-trade.maturity)
    
    elif trade.asset_class == "FX":
        return 0.02 * trade.notional
    
    return 0.0
