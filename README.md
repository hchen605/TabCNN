# tab-cnn

### Guitar Tablature Estimation with a Convolutional Neural Network



### 0. Requirements

This project was made to be run with Python 2.7 -> Python 3.9. You should have the following libraries/packages installed:
* numpy 1.19
* scipy 1.7
* pandas 1.3
* jams 0.3
* librosa 0.8
* keras 2.6
* tensorflow 2.6

### 1. Download dataset

Download the GuitarSet audio and annotation data from [here](https://zenodo.org/record/1422265/files/GuitarSet_audio_and_annotation.zip?download=1 "GuitarSet download"). (Thanks again to the authors for creating this awesome dataset!)

Unzip and place the downloaded GuitarSet folder in `tab-cnn/data/` so that in `tab-cnn/data/GuitarSet/` you have the following two folders:
* `annotation/`
* `audio/`

The remaining instructions assume that you are in the `tab-cnn/` folder.

### 2. Preprocess audio

Run the following line to preprocess different spectral representations for the audio files: 

  `bash data/Bash_TabDataReprGen.sh`

This will save the preprocessed data as compressed numpy (.npz) files in the `data/spec_repr/` directory.


### 3. Train and test model

Run the following line to train and test the TabCNN model:

`python model/TabCNN.py`

A summary log and a csv results file will be saved in a time-stamped folder within the `model/saved/` directory. Additionally, a folder for each fold of data will be created, containing the individual model's weights and predictions. 











