Neural Diary: A method to generate captions of relevant frames from a video clip to give a summary of the clip

To run:
./get_frames.py <movie clip>	//select 1 out of 20 frames from a movie clip and dump in the folder <test>
./get_samples			//analyse the selected frames for relevant frames and dump the selected frames in folder <target>
./get_captions			//processes the files in folder <target> and pass them to Show and Tell to generate captions in the file captions.txt
./get_json:			//processes the output into relevant json file
./test.sh 			//generate captions for the frames selected and process the output to result.json. later, this starts a server which can be visited on 172.27.19.28:9000

Implicit scripts:
get_weights.py: This compares 2 images and returns the L5 norm of the final parameters after forwarding the image on the VGG16 network. the weights are derived from ImageNet dataset 2014
get_csv: process the csv file