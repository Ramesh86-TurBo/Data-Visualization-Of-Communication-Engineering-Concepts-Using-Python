# Author: Ramesh Pai

# Affiliation: 201104047, TE-E&TC Engg, Sem.5, 2021-22, GCE.

# importing python modules
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftshift

# vc: amplitude of Carrier Signal
# m: modulation index of FM Signal
# fc: frequency(Hz) of Carrier Signal 
# fm: frequency(Hz) of Message Signal

def values(vc, m, fc, fm):

    fs = 60000 #sampling frequency
    dt = 1/fs #sample time interval or time-steps for time-domain signal
    t = np.arange(0, 1, dt) #time indices for time-domain signal
    n = np.size(t) #number of samples
    df = fs/n #frquency interval or frequency-steps for frequency-spectrum
    f = np.arange(-fs/2, fs/2, df) #frequency indices for frquency-spectrum

    # plot1: Tone modulated FM Signal v/s Time

    v_fm = vc*np.cos(2*np.pi*fc*t + m*np.sin(2*np.pi*fm*t)) #FM Signal
    plt.subplot(3, 1, 1)
    plt.plot(t, v_fm)
    plt.title("Frequency Modulated Signal", loc='left')
    plt.xlabel("time(sec)", loc='right')
    plt.ylabel("v_fm(volts)")

    # plot2: Spectrum of FM signal v/s Frequency

    xf_1 = fftshift(fft(v_fm)) #FFT of FM Signal(Complex in nature).
    plt.subplot(3, 1, 2)
    plt.plot(f, abs(xf_1)/n) #PLotting frequency indices v/s Normalised magnitude of FFT of FM signal
    plt.xlim(-200, 200)
    plt.title("Spectrum of FM signal", loc='left')
    plt.xlabel("frequency(Hz)", loc='right')
    plt.ylabel("Magnitude")

    # plot3: Spectrum of FM signal v/s Frequency(ZOOMED)

    xf_1 = fftshift(fft(v_fm)) #FFT of FM Signal(Complex in nature).
    plt.subplot(3, 1, 3)
    plt.plot(f, abs(xf_1)/n) #PLotting frequency indices v/s Normalised magnitude of FFT of FM signal
    plt.xlim(30, 70) #for (mf = 1)
    # plt.xlim(10, 90) #for (mf = 2.4)
    # plt.xlim(10, 90) #for (mf = 4)
    plt.title("Spectrum of FM signal(ZOOMED)", loc='left')


    if m == 1:
        plt.title(f"(mf={m}) Bandwidth={fm*4} Hz", loc='right', fontsize = 10, fontstyle = 'italic')
    elif m == 2.4:
        plt.title(f"(mf={m}) Bandwidth={fm*6} Hz", loc='right', fontsize = 10, fontstyle = 'italic')
    elif m == 4:
        plt.title(f"(mf={m}) Bandwidth={fm*10} Hz", loc='right', fontsize = 10, fontstyle = 'italic')


    plt.xlabel("frequency(Hz)", loc='right')
    plt.ylabel("Magnitude")


    plt.subplot_tool()
    plt.show()

values(2, 1, 50, 5) #assigning values to parameters(mf = 1)
# values(2, 2.4, 50, 5) #assigning values to parameters(mf = 2.4)
# values(2, 4, 50, 5) #assigning values to parameters(mf = 4)