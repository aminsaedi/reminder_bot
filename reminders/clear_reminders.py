import yaml
import pathlib

def clear():
	current_path = str(pathlib.Path(__file__).parent.absolute())

	with open(current_path + '/data.yml', 'r') as file:
		data = yaml.safe_load(file)

	for x in range(7):
		data[x] = []
    #for i in range(7):
    #    data[i] = []
    with open(current_path + '/data.yml', 'w') as file:
		try:
			file.truncate(0)
			yaml.dump(data, file)
		except:
			print("Error on writing to file")
