# Low-Latency Neutron-Gamma PSD using Pulse-Coupled and Convolutional Neural Networks

<b>Authors:</b> Fabrizio Chinu, Marcello Di Costanzo, Valerio Pagliarino <br>
All the authors equally contributed to the project.

Project for MFN0824 Reti Neurali - Physics Dept. - University of Turin - prof. M. Osella

In this work a deep learning-based technique using Pulse-Coupled Neural Networks (PCNN) and Convolutional Neural Networks (CNN) is applied to a neutron-gamma Pulse Shape Discrimination (PSD) task. The model is provided with a digitized signal from a scintillator coupled with SiPM. After a post-training analysis of the CNN model, the transfer learning approach is used to investigate the applicability to other particle detectors. Finally, the CNN model is compressed, quantized and deployed on Field Programmable Gate Array real-time electronics. The final model, on a balanced dataset of 9324 items, obtained an accuracy of 99.98 $\mathbf{\pm}$ 0.02 \% in binary classification with the same detector. An accuracy of 98.28 \% and 99.83 \% is obtained after the transfer learning, targeting two different particle detector.


<img src="https://github.com/valeriopagliarino/Neutron-Gamma-PSD-2023-UNITO/blob/main/figures/arc.png" width=800>

### Downloading the datasets

#### DATASET 1:
Paper: https://link.springer.com/article/10.1007/s41365-022-01054-6 <br>
Dataset: https://www.scidb.cn/en/detail?dataSetId=327d6ec5119b46cf84b61b2be0300471

``` bash
wget https://china.scidb.cn/download?fileId=e92e5dcac193d006e9dfd8096fb005ed&traceId=9407e6dc-2e78-4540-b69b-026c8437c143 -O ./dataset1.zip
tar –xvzf ./dataset1.zip
```

#### DATASET 2:
Dataset: https://www.scidb.cn/en/detail?dataSetId=8f91b76e2552410da914911b5d889d21

``` bash
wget https://china.scidb.cn/download?fileId=63e1e798f4ef407916cadc47&traceId=9407e6dc-2e78-4540-b69b-026c8437c143 -O ./dataset2.zip
tar –xvzf ./dataset2.zip
```

#### DATASET 3:
 
Data from: https://github.com/NeutronNeutrinoSensing/PSDwithML <br>
Download the dataset from Dropbox: https://www.dropbox.com/sh/sklqbrd7gvq6azz/AABCExrGTyESctHbs1eQO4m6a?dl=0
<br>put the files inside a folder named ./dataset3


#### DATASET 4:

Data from: https://github.com/NeutronNeutrinoSensing/PSDwithML

``` bash
git clone https://github.com/NeutronNeutrinoSensing/PSDwithML
mkdir dataset4
mv ./PSDwithML/data/* ./dataset4
rm -r ./PSDwithML
```

### Configuring the Environment:

#### Python3 env for Neural Network training

``` bash
virtualenv                        20.16.4
visualkeras                       0.0.2
tensorboard                       2.11.2
tensorboard-data-server           0.6.1
tensorboard-plugin-wit            1.8.0
tensorflow                        2.11.0
tensorflow-datasets               4.4.0
tensorflow-estimator              2.11.0
tensorflow-gpu                    2.7.0
tensorflow-io-gcs-filesystem      0.31.0
tensorflow-metadata               1.2.0
tensorflow-model-optimization     0.7.3
tensorpac                         0.6.5
sklearn                           0.0
scikit-learn                      1.0.2
scikit-image                      0.18.3
scikit-learn                      0.24.2
scikit-optimize                   0.8.1
scipy                             1.1.0
seaborn                           0.11.2
QKeras                            0.9.0
PyVirtualDisplay                  3.0
pydot                             1.4.2
pip                               23.0.1
notebook                          6.4.0
nteract-on-jupyter                2.1.3
keras                             2.11.0
Keras-Applications                1.0.8
keras-nightly                     2.5.0.dev2021020510
Keras-Preprocessing               1.1.2
keras-rl2                         1.0.5
keras-tuner                       1.3.5
keras-unet                        0.1.2
keras-vis                         0.4.1
MarkupSafe                        2.1.3
matplotlib                        3.5.3
matplotlib-inline                 0.1.6
numpy                             1.21.6
pandas                            1.3.5
```
#### Python3 env for HLS4ML flow

```bash
MarkupSafe                    2.1.3
matplotlib                    3.5.3
matplotlib-inline             0.1.6
numpy                         1.21.6
h5py                          3.8.0
hls4ml                        0.7.1
keras                         2.11.0
keras-tuner                   1.3.5
onnx                          1.14.0
pandas                        1.3.5
pydot                         1.4.2
scikit-learn                  1.0.2
scipy                         1.1.0
tensorboard                   2.11.2
tensorboard-data-server       0.6.1
tensorboard-plugin-wit        1.8.1
tensorflow                    2.11.0
tensorflow-estimator          2.11.0
tensorflow-io-gcs-filesystem  0.32.0
tensorflow-model-optimization 0.7.3
QKeras                        0.9.0
visualkeras                   0.0.2
```
