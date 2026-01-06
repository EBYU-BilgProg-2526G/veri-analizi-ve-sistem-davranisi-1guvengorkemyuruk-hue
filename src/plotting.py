import matplotlib.pyplot as plt

def plot_time(t, x_raw, x_filt, save_path):
    """
    Ham ve filtrelenmiş sinyali zaman domeninde çizer
    """
    plt.figure(figsize=(10, 5))

    plt.plot(t, x_raw, label="Ham Sinyal")
    plt.plot(t, x_filt, label="Filtrelenmiş Sinyal")

    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.title("Zaman Domeninde Sinyal")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
