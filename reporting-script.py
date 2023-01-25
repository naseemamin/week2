#Traverse filesystem finding the largest files in a path
#Make sure paths are not hardcoded

import yaml
import os
import pandas as pd
from os.path import join

#return directory of file where yaml file is located
config_path = os.path.dirname(os.path.abspath(__file__))

#open and read yaml file from directory
def readInConfigSettings(config_path):
    with open (f'{config_path}/config.yaml') as file:
        try:
            config = yaml.safe_load(file)
            return config
        
        except yaml.YAMLError as exec:
            print(exec)
            exit(exec)
          
config = readInConfigSettings(config_path)
folder_path = config["folder_path"]


#Function for traversing filesystem finding the largest file in a path
def find_largest_files(folder_path):
    max_size = 0
    largest_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > max_size:
                largest_files = [(file_path, file_size)]
                max_size = file_size
            elif file_size == max_size:
                largest_files.append((file_path, file_size))
    return largest_files

list_largest = [print(f'This is the largest file: {file_path} : {file_size} bytes') for file_path, file_size in find_largest_files(folder_path)]
    

#Function for traversing filesystem finding the n largest files in a path, max file size in mb
def find_n_largest_files_mb(folder_path, n, max_size):
    n_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_size_mb = file_size / (1024**2)
        if file_size_mb < max_size:  
            n_files.append((file_path, file_size_mb))
    return sorted(n_files, key=lambda x:x[1], reverse=True)[0:n]

list_big_mb = [print(f'{file_path} : {file_size_mb:.2f} megabytes') for file_path, file_size_mb in find_n_largest_files_mb(folder_path, 4,1000000)]
