import os
import pandas as pd
from difflib import get_close_matches
import shutil

HOME = "/home/kevinpatel711/temp_omics/" #temp_omics
LIST = "/home/kevinpatel711/omics_sub_jour_mapping/" #list of journal names
TARGET = "/home/kevinpatel711/omics_sub_wise/"

# df0 = pd.read_csv(LIST)
files = os.listdir(HOME)
links = [file[:-4] for file in files]
frames = os.listdir(LIST)

for frame in frames:
        try:
                os.mkdir(TARGET+frame[:-5])
        except:
                print(frame[:-5]," exists. Will Overwrite.")

for link in links:
        link = " ".join(link.split("_"))
        match = []
        subject = []
        for frame in frames:
                print("Now executing ",frame)

                folder = frame[:-5]
                

                df0 = pd.read_excel(LIST+frame, sheet_name='Sheet1')
                names = df0['Journal Name'].values
                names = [name.lower().strip() for name in names]

                #print("Journal names are", names)

                
                name = get_close_matches(word=link, possibilities=names, n=1, cutoff=0.5)
                match.append(name)
                
        fin = get_close_matches(word=link, possibilities=match, n=1)
        i = match.index(fin)
        print(TARGET+frames[i]+"/"+link+".csv")
        
        try:
                shutil.copy(HOME+link+".csv", TARGET+frames[i][:-5]+"/"+link+".csv")
                
        except:
                print("Failure at ",folder, link, TARGET)



