import yaml
import os

def write(new_yaml_data_dict):

    if not os.path.isfile("NetworkPolicy.yml"):

        with open("NetworkPolicy.yml", "a") as fo:
            fo.write("---\n")
    with open("NetworkPolicy.yml", "a") as fo:
            fo.write("---\n")
    #the leading spaces and indent=4 are key here!
    sdump = yaml.dump(
                new_yaml_data_dict
                ,indent=0,sort_keys=False
                )

    with open("NetworkPolicy.yml", "a") as fo:
        fo.write(sdump)
name  = 'allow-http-and-https'

for i in range(1,10001):
     name = name+'-'+str(i)
     new_yaml_data_dict = {'kind': 'NetworkPolicy', 'apiVersion': 'networking.k8s.io/v1', 'metadata': {'name': name}, 'spec': {'podSelector': {'matchLabels': {'role': 'frontend'}}, 'ingress': [{'ports': [{'protocol': 'TCP', 'port': 80}, {'protocol': 'TCP', 'port': 443}]}]}}
     write(new_yaml_data_dict)
     name = 'allow-http-and-https'

#new_yaml_data_dict = {'kind': 'NetworkPolicy', 'apiVersion': 'networking.k8s.io/v1', 'metadata': {'name': name}, 'spec': {'podSelector': {'matchLabels': {'role': 'frontend'}}, 'ingress': [{'ports': [{'protocol': 'TCP', 'port': 80}, {'protocol': 'TCP', 'port': 443}]}]}}
#write(new_yaml_data_dict)
'''
import yaml
from pathlib import Path
conf = yaml.safe_load(Path('NetworkPolicy.yml').read_text())
print(conf)
'''