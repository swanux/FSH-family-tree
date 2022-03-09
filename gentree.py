import json, sys

def open_json_file():
	file = open(sys.argv[1], 'r')
	data = json.load(file)
	file.close()
	return data

def gendb():
	data = open_json_file()
	dwellerdb = {}

	for line in data["dwellers"]["dwellers"]:
		line['relations']['descendants'] = []
		line['relations']['spouses'] = []
		dwellerdb[line['serializeId']] = line

	for line in data["dwellers"]["dwellers"]:
		sid = line['serializeId']
		relations = line["relations"]['ascendants']
		gender = 'M' if line['gender'] == 2 else 'F'
		dwellerdb[sid]["gender"] = gender
		if relations[0] != -1:
			dwellerdb[relations[0]]['relations']['descendants'].append(sid)
			dwellerdb[relations[1]]['relations']['descendants'].append(sid)
			
			if relations[1] not in dwellerdb[relations[0]]['relations']['spouses']:
				dwellerdb[relations[0]]['relations']['spouses'].append(relations[1])
			if relations[0] not in dwellerdb[relations[1]]['relations']['spouses']:
				dwellerdb[relations[1]]['relations']['spouses'].append(relations[0])

	f = open('dwellerdb.yaml', 'w')
	content = ""
	unions = {}
	for key, value in dwellerdb.items():
		for key2, value2 in value['relations'].items():
			if key2 == 'spouses':
				for value3 in value2:
					try: unions[f"{key} - {value3}"]
					except:
						try: unions[f"{value3} - {key}"]
						except: unions[f"{key} - {value3}"] = []
			elif key2 == 'ascendants':
				try: unions[f"{dwellerdb[key]['relations']['ascendants'][0]} - {dwellerdb[key]['relations']['ascendants'][1]}"]
				except:
					try: unions[f"{dwellerdb[key]['relations']['ascendants'][1]} - {dwellerdb[key]['relations']['ascendants'][0]}"]
					except: unions[f"{dwellerdb[key]['relations']['ascendants'][0]} - {dwellerdb[key]['relations']['ascendants'][1]}"] = []
				try: unions[f"{dwellerdb[key]['relations']['ascendants'][0]} - {dwellerdb[key]['relations']['ascendants'][1]}"].append(key)
				except: unions[f"{dwellerdb[key]['relations']['ascendants'][1]} - {dwellerdb[key]['relations']['ascendants'][0]}"].append(key)
	content += "families:\n"
	for key, value in unions.items():
		content += f"  - parents: [{key.split(' - ')[0]}, {key.split(' - ')[1]}]\n"
		childlist = []
		for i in value:
			childlist.append(i)
		content += f"    children: {childlist}\n"
	content += "\n\npeople:\n"
	for key, value in dwellerdb.items():
		content += f"  {key}:\n    name: {value['name']} {value['lastName']}\n    fullname: ID is {key}\n    class: [{value['gender']}]\n"
	content = content.replace("-1]", "-2]")
	content += "  -1:\n    name: Adam\n    fullname: None\n    class: [M]\n"
	content += "  -2:\n    name: Eve\n    fullname: None\n    class: [F]\n\n\n"
	content += "styles:\n  M:\n    shape: rectangle\n    color: blue\n  F:\n    shape: ellipse\n    color: red\n"
	f.write(content)
	f.close()


if __name__ == "__main__":
	if ".json" not in sys.argv[1]:
		print("Please provide a json file as an argument.")
	else:
		gendb()