import scipy.io.wavfile
from scipy.signal import decimate
import numpy as np
import warnings
import sys


def convert_to_mono(signal):

    try:
        signal = [int((s[0] + s[1])/2) for s in signal]
        return signal
    except:
        return signal


def hps(signal, w):
    num_of_windows = 3
    
    if(num_of_windows > len(signal) / w): num_of_windows = len(signal) / w
    
    windows = [signal[i * w : (i+1) * w] for i in range(int(num_of_windows))]
    result = []
    sum_male = 0
    sum_female = 0
    for window in windows:
        #frame = np.kaiser(len(window), 5)
        #window = window * frame
        fft = np.fft.fft(window)
        fft = abs(fft)/(0.5 * w)
        fft_copy = np.copy(fft)
        for i in np.arange(2, 5):
            d = decimate(fft, int(i))
            fft_copy[: len(d)] *= d
        result.append(fft_copy)
    
    for x in result:
        sum_male += sum(x[60:161])
        sum_female += sum(x[180:271])

    if sum_male > sum_female: return 'M'
    else: return 'K'

def process(file):

    try:
        w, signal = scipy.io.wavfile.read(file)
        warnings.filterwarnings('ignore')
    except:
        return 'K'
    
    signal = convert_to_mono(signal)
    return hps(signal, w)

if __name__=='__main__':

    try:
        print(process(sys.argv[1]))
    except:
        print("K")
    