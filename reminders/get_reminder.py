import yaml
import pathlib
from datetime import datetime

def by_day_of_week(day_of_week):
	current_path = str(pathlib.Path(__file__).parent.absolute())
	with open(current_path + '/data.yml', 'r') as file:
		data = yaml.safe_load(file)
	
	today = str(day_of_week)
	today = str(datetime.now().weekday())
	if day_of_week != None:
		today = str(day_of_week)
	return data[today]
