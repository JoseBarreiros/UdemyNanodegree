import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
import shutil
import pdb

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    split_ratio=0.7
    allFileNames = os.listdir(data_dir)
    
    #shuffle data
    np.random.shuffle(allFileNames)
    #split dataset
    train_FileNames, val_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)*split_ratio)])
    train_FileNames = [data_dir+ name for name in train_FileNames.tolist()]
    val_FileNames = [data_dir + name for name in val_FileNames.tolist()]
    print('Total files: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Validation: ', len(val_FileNames))
    
    # Move files
    parent_directory=os.path.dirname(os.path.dirname(data_dir))
    pdb.set_trace()
    for name in train_FileNames:
        shutil.move(name, os.path.join(parent_directory,"train",os.path.basename(name)))
    for name in val_FileNames:
        shutil.move(name, os.path.join(parent_directory,"val",os.path.basename(name)))
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)