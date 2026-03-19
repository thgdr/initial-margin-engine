import numpy as np

CORRELATION_MATRIX = {
    ("Short", "Short"): 1.0,
    ("Short", "Medium"): 0.7,
    ("Short", "Long"): 0.5,
    ("Medium", "Medium"): 1.0,
    ("Medium", "Long"): 0.8,
    ("Long", "Long"): 1.0,
}

def get_correlation(b1, b2):
    return CORRELATION_MATRIX.get((b1, b2)) or CORRELATION_MATRIX.get((b2, b1)) or 0.0