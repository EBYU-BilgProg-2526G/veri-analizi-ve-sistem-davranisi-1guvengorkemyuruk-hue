import numpy as np

def sampling_rate(t):
    """
    Zaman vektöründen örnekleme frekansını hesaplar
    """
    t = np.asarray(t)

    # Ardışık zaman farkları
    dt = np.diff(t)

    # Ortalama örnekleme aralığı
    dt_mean = np.mean(dt)

    fs = 1.0 / dt_mean
    return fs


def basic_stats(x):
    """
    Sinyal için temel istatistikleri hesaplar
    """
    x = np.asarray(x)

    stats = {
        "mean": np.mean(x),
        "std": np.std(x),
        "rms": np.sqrt(np.mean(x**2)),
        "min": np.min(x),
        "max": np.max(x)
    }

    return stats
