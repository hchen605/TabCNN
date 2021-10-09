import os
import numpy as np
import jams
from scipy.io import wavfile
import sys
#import librosa
#from keras.utils import to_categorical
#from tensorflow.keras.utils import to_categorical #HH


# returns the filename with no extension
path = "GuitarSet/"
path_anno = path + "annotation/"
filenames = np.sort(np.array(os.listdir(path_anno)))
#filenames = filter(lambda x: x[-5:] == ".jams", filenames)
#print(filenames.dtype)
print(filenames.size)
print(filenames)



