import os
import pickle
import numpy as np


def get_dataset(size=100, max_value=100):
    dataset = None
    dataset_dir = f'{os.getcwd()}/dataset'

    if not os.path.isfile(dataset_dir):
        with open(dataset_dir, 'wb') as file:
            dataset = np.random.randint(max_value, size=(size))
            pickle.dump(dataset, file)
            print('Dataset generated.')
    else:
        with open(dataset_dir, 'rb') as file:
            dataset = pickle.load(file)
            print('Dataset loaded.')
    
    return dataset
