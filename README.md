# Data-Visualization-Of-Communication-Engineering-Concepts-Using-Python

Libraries used: Matplotlib, Numpy, Scipy

A) EXP1: To simulate Amplitude Modulation(AM) & Demodulation using Python

Concept: 
Amplitude Modulation (AM) is a technique that encodes information by varying the amplitude of a high-frequency carrier signal based on a lower-frequency message signal. Demodulation is the process of extracting the original message signal from the modulated carrier signal.

Program Details: 
1. The program imports the necessary modules: `matplotlib.pyplot`, `numpy`, and `scipy.fft`.
2. The `values` function takes six parameters: `vm1`, `vm2`, `vc`, `fm1`, `fm2`, and `fc`.
3. Various variables are initialized, including the sampling frequency, time step, time indices, number of samples, frequency step, and frequency indices.
4. The program plots the message signal, carrier signal, and modulated signal.
5. The frequency spectrum of the modulated signal is computed using the FFT, and its magnitude is plotted against frequency.
6. The demodulated signal is obtained by multiplying the modulated signal with the carrier signal, and both the signal and its frequency spectrum are plotted.
7. A filter is designed to extract the original two-tone signal.
8. The filtered spectrum is obtained by multiplying the demodulated signal's frequency spectrum with the filter.
9. The inverse FFT is applied to the filtered spectrum to obtain the original two-tone signal in the time domain.
10. The demodulated two-tone signal is plotted against time.
11. The `values` function is called with specific parameter values to generate the plots.


B) EXP3: To simulate Frequency Division Multiplexing (FDM) & Demultiplexing using Python

Concept:
FDM (Frequency Division Multiplexing) is a method to transmit multiple signals simultaneously by dividing the frequency spectrum into subbands. Demultiplexing is the process of separating the signals at the receiving end, allowing each signal to be retrieved from the shared transmission.

Program Details:
1. The program imports the necessary modules: `matplotlib.pyplot`, `numpy`, and `scipy.fft`.
2. The `values` function takes four parameters: `vm1`, `vm2`, `fm1`, and `fm2`.
3. Various variables are initialized, including the sampling frequency, time step, time indices, number of samples, frequency step, and frequency indices.
4. The program plots the first message signal, second message signal, and their frequency spectra.
5. The frequency division multiplexing (FDM) signal is obtained by adding the frequency spectra of the two message signals.
6. Two filters are designed to extract the individual message signals.
7. The first message signal is demultiplexed by multiplying the FDM signal with the first filter and performing an inverse FFT to obtain the original signal in the time domain. The demultiplexed signal is plotted.
8. The second message signal is demultiplexed in a similar manner using the second filter, and the demultiplexed signal is plotted.
9. The plots are displayed.
10. The `values` function is called with specific parameter values to generate the plots.



C) EXP4: To simulate Frequency Modulation (FM) using Python

Concept:
FM (Frequency Modulation) is a modulation technique where the frequency of a carrier signal is varied based on the amplitude of a modulating signal. Demodulation is the process of extracting the original modulating signal from the FM carrier signal.

Program Details:

