#!/usr/bin/env python
import re
import json

input_file = open('captions.txt')
raw_data = input_file.readlines()
raw_data = raw_data[1:]

new_dict = dict()

for i in range(0, len(raw_data), 4):
	test = raw_data[i]
	test = re.sub('Captions for image ', '', test)
	test = re.sub(':\n', '', test)
	dict1 = {test: [raw_data[i+1].strip(), raw_data[i+2].strip(), raw_data[i+3].strip()]}
	new_dict.update(dict1)

with open('result.json', 'w') as fp:
	json.dump(new_dict, fp)