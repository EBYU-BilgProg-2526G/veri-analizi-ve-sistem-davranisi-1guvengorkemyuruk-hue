# -*- coding: utf-8 -*-
"""
Ana çalışma dosyası
Öğrenciler bu dosyayı çalıştıracaktır.
"""

from io_utils import load_signal_csv
from analysis import sampling_rate, basic_stats
from signal_tools import moving_average
from plotting import plot_time

def main():
    # 1. CSV dosyasını oku
    csv_path = "../data/sample_signal.csv"
    t, x = load_signal_csv(csv_path)

    # 2. Örnekleme frekansını hesapla
    fs = sampling_rate(t)
    print(f"Örnekleme Frekansı (fs): {fs:.2f} Hz")

    # 3. Temel istatistikleri yazdır
    stats = basic_stats(x)
    print("Temel İstatistikler:")
    for key, value in stats.items():
        print(f"{key}: {value:.4f}")

    # 4. Hareketli ortalama filtresi uygula
    window_size = 10
    x_filt = moving_average(x, window_size)

    # 5. Sonucu çizdir
    save_path = "signal_time_plot.png"
    plot_time(t, x, x_filt, save_path)

    print(f"Grafik kaydedildi: {save_path}")


if __name__ == "__main__":
    main()
