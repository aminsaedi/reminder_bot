import yaml
import pathlib

def add_for_day(task_name, day_of_week):
	current_path = str(pathlib.Path(__file__).parent.absolute())
	print(task_name, day_of_week)

	with open(current_path + '/data.yml', 'r') as file:
		data = yaml.safe_load(file)
	with open(current_path + '/data.yml', 'r+') as file:
		try:
			data[day_of_week].append(task_name)
			file.truncate(0)
			yaml.dump(data, file)
		except:
			print("Error on writing to file")
		#yaml.dump(data,file)
