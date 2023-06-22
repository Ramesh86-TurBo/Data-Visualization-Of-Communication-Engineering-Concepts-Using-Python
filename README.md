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
1. Import the required Python modules: `matplotlib.pyplot` for plotting and `numpy` for numerical operations.
2. Import the `fft` and `fftshift` functions from `scipy.fft` module for Fourier transform calculations.
3. Define a function `values` that takes four parameters: `vc` (amplitude of the carrier signal), `m` (modulation index of the FM signal), `fc` (frequency of the carrier signal), and `fm` (frequency of the message signal).
4. Set the sampling frequency (`fs`), the sample time interval (`dt`), and create an array of time indices (`t`) for the time-domain signal.
5. Calculate the frequency interval (`df`) and create an array of frequency indices (`f`) for the frequency spectrum.
6. Generate the Frequency Modulated (FM) signal `v_fm` using the provided formula: `vc * np.cos(2*np.pi*fc*t + m*np.sin(2*np.pi*fm*t))`.
7. Plot the FM signal in the time domain using `plt.plot`.
8. Calculate the Fast Fourier Transform (FFT) of the FM signal (`v_fm`) and shift the frequency components using `fftshift`.
9. Plot the spectrum of the FM signal in the frequency domain using `plt.plot`.
10. Create a zoomed-in view of the spectrum and annotate the bandwidth based on the modulation index and message frequency.
11. Execute the function `values` with specific parameter values to generate and analyze the FM signal.



D) EXP8: To simulate Pulse Code Modulation (PCM) using Python

Concept:
PCM is a digital modulation technique that converts analog signals into digital form. It involves sampling, quantizing, encoding, and decoding the signal. It provides high fidelity and noise immunity for applications like telecommunications and audio recording.

Program Details:
1. Import the required Python modules: 
   - `matplotlib.pyplot` for plotting graphs
   - `numpy` for numerical computations
   - `scipy.fft` for fast Fourier transform operations
2. Define the function `values(vm, fm, bits)` that takes three parameters:
   - `vm`: Amplitude of the message signal
   - `fm`: Frequency of the message signal
   - `bits`: Number of bits per sample
3. Set the sampling frequency (`fs`), time step (`dt`), time indices (`t`), and frequency indices (`f`) for the signals.
4. Plot the message signal in the time domain:
   - Generate the message signal using `v_m = vm*np.sin(2*np.pi*fm*t)`
   - Create a subplot and plot the message signal using `plt.plot(t, v_m)`
5. Quantize the message signal:
   - Shift the message signal by `vm` to make quantization easier (`v_m_shifted = v_m + vm`)
   - Determine the number of levels (`L`) based on the number of bits per sample
   - Calculate the step size (`stepSize`) for quantization
   - Create a list of quantization levels (`qLevelList`)
   - Iterate over the shifted message signal and assign the quantized values to `qSignal`
6. Plot the quantized signal in the time domain:
   - Create a subplot and plot the quantized signal and the original signal (`v_m_shifted`) using `plt.plot(t, qSignal)` and `plt.plot(t, v_m_shifted, linestyle='dotted', color='r')`
7. Encode and decode the quantized values:
   - Create an empty list (`enCodedList`) to store the encoded values
   - Iterate over the quantized values and assign the corresponding code number to each value
   - Convert the code numbers to binary and store them in `enCodedList`
   - Create an empty list (`deCodedList`) to store the decoded values
   - Iterate over the encoded values and convert them back to decimal, storing them in `deCodedList`
8. Reconstruct the signal:
   - Subtract `vm` from the quantized signal to reconstruct the signal (`v_m_reconstructed = qSignal - vm`)
9. Plot the reconstructed signal in the time domain:
   - Create a subplot and plot the reconstructed signal using `plt.plot(t, v_m_reconstructed)`
10. Filter the reconstructed signal to recover the original signal:
    - Define a filter that attenuates frequencies outside the range of the original signal
    - Apply the filter to the spectrum of the reconstructed signal using fast Fourier transform operations
    - Perform an inverse Fourier transform on the filtered spectrum to obtain the recovered signal
    - Plot the recovered signal and the original signal in a subplot using `plt.plot(t, v_m_recovered)` and `plt.plot(t, v_m, color='r', linestyle='dotted')`



E) EXP8: To simulate Binary Amplitude Shift Keying (ASK) using Python

Concept:
Binary Amplitude Shift Keying (ASK) is a modulation technique that uses different amplitude levels to represent binary data, making it a simple and commonly used method in digital communication.

Program Details:





