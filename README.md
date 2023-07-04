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
