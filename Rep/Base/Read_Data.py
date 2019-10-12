import yaml, os

def ret_yaml_data(file_name):
    file_path = os.getcwd() + os.sep + "Data" + os.sep +file_name + ".yml"
    with open(file_path,"r") as f:
        return yaml.load(f)