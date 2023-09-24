from modules import *
from source import *

def data():
    with open("src/data.yaml","r") as file:
        getyaml = yaml.load(file, Loader=yaml.FullLoader)
    return getyaml

