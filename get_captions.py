import subprocess
import os
import re
import sys

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    l.sort(key=alphanum_key)

sample_folder='/data/gpuuser2/neuraldiary/Sampled'
files = os.listdir(sample_folder)
print 'Found ' + str(len(files)) + ' in the folder ' + sample_folder + '. Sorting...'
sort_nicely(files)

filepath =  []
for entity in files:
    filepath.append('/data/gpuuser2/neuraldiary/dummy/'+entity)

text = ','.join(filepath)

vocab="/data/gpuuser2/models/word_counts.txt"
checkpoint="/data/gpuuser2/models/model/train"

os.chdir("/data/gpuuser2/models/im2txt")

p=subprocess.Popen(["bazel-bin/im2txt/run_inference","--checkpoint_path="+checkpoint,"--vocab_file="+vocab,"--input_files="+text],stdout=subprocess.PIPE)

sys.stdout = open('/data/gpuuser2/neuraldiary/captions.txt','w')
print p.communicate()[0]