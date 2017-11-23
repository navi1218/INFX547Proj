import json

file = open('Hashtag_glossier.json', 'r')

json_objects = []

for line in file:
	while True:
		try:
			json_obj = json.loads(line)
			break
		except ValueError:
			# Not yet a complete JSON value
			try:
				line += next(file)
			except StopIteration:
				print("reached end of file")
				break
	json_objects.append(json_obj)