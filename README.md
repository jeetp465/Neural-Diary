# Neural Diary: Forming compressed visual stories

The Neural Diary is a course project for **CS698O:Visual Recognition**
# Dependencies
[Show and Tell: A Neural Image Caption Generator](https://github.com/tensorflow/models/tree/master/im2txt)

Save the model in models folder in the same directory you save this repository. Follow the preprocessing instructions as described in the link. It uses MSCOCO dataset to train the LSTM model built on top of a Inceptionv3 model pre-trained on ImageNet dataset.

A Caffe implementation of **VGG-16** model to obtain the **fc7** features of frames.

# To run
`chmod +x *.py` Converts python files into executables

`./get_frames.py <movie clip>`	Selects 1 out of 20 frames from a movie clip and dump in the folder **Frames**

`./get_samples`	Analyse the selected frames for relevant frames and dump the selected frames in folder **Sampled**

`./get_captions` Processes the files in folder **Sampled** and pass them to Show and Tell to generate captions in the file captions.txt

`./get_json` Processes the output into relevant json file.

`./test.sh` Generate captions for the frames selected and process the output to result.json. Later, this starts a server which can be visited on 172.27.19.28:9000 (your local address in your case)

## Implicit scripts:
`get_weights.py` This script compares 2 images and returns the L5 norm of the final parameters after forwarding the image on the VGG16 network. The weights are derived from ImageNet dataset 2014.