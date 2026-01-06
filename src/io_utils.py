import csv
import numpy as np

def load_signal_csv(path):
    """
    CSV formatı:
    t,x
    0.0, 1.23
    0.01, 1.10
    ...

    Parametre:
        path (str): CSV dosya yolu

    Dönen:
        t : zaman vektörü (numpy array)
        x : sinyal vektörü (numpy array)
    """
    t = []
    x = []

    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # başlık satırını atla (t,x)

        for row in reader:
            t.append(float(row[0]))
            x.append(float(row[1]))

    return np.array(t), np.array(x)
