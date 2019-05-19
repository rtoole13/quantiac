import zipfile
import os

import pandas as pd

def unzip_ticker_data(source="tickerData.zip", destination="."):
    with zipfile.ZipFile(source, 'r') as zip_ref:
        zip_ref.extractall(destination)
        zip_ref.close()
        
def make_ticker_dict(source="tickerData", data_subset=None):
    data_dict = {}
    
    files_in_directory = os.listdir(source)
    if not data_subset:
        data_subset = files_in_directory
        
    for filename in files_in_directory:
        if filename[:-len(".txt")]  in data_subset:
            df = pd.read_table(os.path.join(source, filename), sep=",")
            df["DATE"] = pd.to_datetime(df["DATE"], format="%Y%m%d")
            df = df.set_index("DATE")
            data_dict[filename[:filename.find(".txt")]] = df
            
    return data_dict