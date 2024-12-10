import pandas as pd
import xlrd 
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import glob
import EntropyHub as EH
import pywt
import os

#path_to_VA = "C:/Users/HP/OneDrive - Indian Institute of Technology Bhubaneswar/BTP_Drive/DATASET-2. VA2-20241204T052628Z-001.zip/2. VA2"


def extract(path_to_VA2):
    path_to_VA2 = path_to_VA2 + "/*.xlsx"
    excel_files = glob.glob(path_to_VA2)

    data = []

    for file in excel_files:
        df = pd.read_excel(file)
        wavelet = 'db4'
        coeffs_epy = pywt.wavedec(df['es'], wavelet, level=4)
        df= df['es'].dropna().values[2000:]
        cA_1 = np.array(coeffs_epy[0]).flatten()
        cA_2 = np.array(coeffs_epy[1]).flatten()
        cA_3 = np.array(coeffs_epy[2]).flatten()
        cA_4 = np.array(coeffs_epy[3]).flatten()
        cA_5 = np.array(coeffs_epy[4]).flatten()


        
        data.append((cA_1, cA_2, cA_3, cA_4,cA_5))
    print(len(excel_files))
    return data


