from tqdm.auto import tqdm
import multiprocessing as mp
import numpy as np
import pandas as pd
import os
from datetime import datetime
import pytz
import matplotlib.pyplot as plt

import gc


import warnings
warnings.filterwarnings('ignore')


############# PANDAS #####################

def _initialize_mp():
    cores = mp.cpu_count()
    print(f"Making processes faster with {cores} cores!")
    return cores


def pd_parallel_apply(Series, fun):
    cores = _initialize_mp()
    split_ser = np.array_split(Series, cores)
    with mp.Pool(cores) as p:
        app = pd.concat(p.map(fun, split_ser), axis=0)

    return app

def df_reduce_memory(df):
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type != object:
            cmin = df[col].min()
            cmax = df[col].max()
            if str(col_type)[:3] == 'int':
                if cmin > np.iinfo(np.int8).min and cmax < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif cmin > np.iinfo(np.int16).min and cmax < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif cmin > np.iinfo(np.int32).min and cmax < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif cmin > np.iinfo(np.int64).min and cmax < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if cmin > np.finfo(np.float16).min and cmax < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif cmin > np.finfo(np.float32).min and cmax < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    return df



## show any image with given size
def show_image(img, size=(8,8)):
    plt.figure(figsize=size)
    
    while img.shape[0] == 1:
        img = img[0]
    

    if (len(img.shape) == 2) or (img.shape[-1] == 1):
        plt.imshow(img, cmap='gray')
    elif len(img.shape) == 3:
        plt.imshow(img[:, :, ::-1])
        
    plt.show()
    
    
    
def get_current_time(utc=False):
    TZ = pytz.timezone('Asia/Kolkata') if not utc else pytz.utc
    return datetime.now(TZ).strftime('%Y:%m:%d %H:%M:%S %Z %z')
    
# garbage collect
def gc_clear():
    gc.collect()
    for _ in range(10):
        s = gc.collect()
