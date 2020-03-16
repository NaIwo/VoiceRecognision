
## VoiceRecognision

This app try to recognise the sex of speaking person. It is simple concept based on Fast Fourier Transformation and decimate function with a pre-cleaning data. The signal is cut and analysing as an independent windows. Algorithm was tested on not too much noisy data and reached 96% accuracy.

# Usage

Download script and use data similar to 01_K.wav and 02_M.wav

In terminal, type:
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


## Collaborator:

<a href="https://github.com/BartekPrz"><img src="https://avatars3.githubusercontent.com/u/38264818?s=400&v=4" title="BartekPrz" width="80" height="80"></a>
