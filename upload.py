import requests
from os import listdir
from os.path import isfile, join
import json

files = [f for f in listdir(".\directory_path") if isfile(join(".\directory_path", f))]

for file in files:
	url = "http://posturl" + file.replace(".json","")

	with open(".\directory_path\\"+file, 'rb') as f:
			parsed = json.loads(f.read())

	print(requests.post(url, json=parsed))
	#print(json.dumps(parsed, indent=4, sort_keys=True))