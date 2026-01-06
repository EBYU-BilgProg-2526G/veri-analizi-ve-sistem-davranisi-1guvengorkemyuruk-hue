import numpy as np

def moving_average(x, window_size):
    """
    Hareketli ortalama filtresi
    """
    x = np.asarray(x)
    y = []

    for i in range(len(x)):
        start = max(0, i - window_size + 1)
        window = x[start:i + 1]
        y.append(np.mean(window))

    return np.array(y)
