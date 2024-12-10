import os
import glob
from datetime import datetime

# Set path to the folder containing your Excel files
#folder_path = r"C:\Users\HP\OneDrive - Indian Institute of Technology Bhubaneswar\BTP_Drive\DATASET-2. VA2-20241204T052628Z-001\2. VA2\E"



def get(folder_path):
        excel_files = glob.glob(os.path.join(folder_path, "*.xlsx"))  # Get all Excel files in the folder
        print(len(excel_files))
        column = []
    
        for i, file_path in enumerate(excel_files):
            # Get the base directory and file name
            base_dir = os.path.dirname(file_path)
            old_file_name = os.path.basename(file_path)
            name, ext = os.path.splitext(old_file_name)  # Separate the name and extension
            c = f"{name[:6]}"  # Incremental index
            column.append(c)
        return column

            
          