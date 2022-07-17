import yaml
import pathlib


def clear():
    current_path = str(pathlib.Path(__file__).parent.absolute())
    with open(current_path + '/data.yml', 'r') as file:
        data = yaml.safe_load(file)
        print(data)
    for i in range(7):
        data[str(i)] = []
    print(data)
    with open(current_path + '/data.yml', 'w') as file:
        yaml.dump(data, file)

