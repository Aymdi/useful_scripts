'''
For converting mat files to csv files
'''

import os
import scipy.io
import pandas as pd

DIR = os.getpwd()

def mat2csv(dire_name, file_name):
    """generate csv file from mat file

    Args:
        dire_name (string): directory name
        file_name (string): file name without extension
    """    
    mat = scipy.io.loadmat(dire_name+file_name+'.mat')
    mat = {k:v for k, v in mat.items() if k[0] != '_'}
    data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
    data.to_csv(dire_name+file_name+'.csv')
    
