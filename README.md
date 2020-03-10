
## VoiceRecognision

This app try to recognise the sex of speaking person. It is simple concept based on Fast Fourier Transformation and decimate function with a pre-cleaning data. The signal is cut and analysing as a indipendent window. Algorithm was tested on not to much noicy data and get accuraccy about 96%.

# Usage

Download script and use data similar to 01_K.wav and 02_M.wav

Type in terminal:
```bash
> python voice_recognision.py 01_K.wav
```
and wait for results.

# Required packages

```python
import scipy.io.wavfile
from scipy.signal import decimate
import numpy
import warnings
import sys
```
