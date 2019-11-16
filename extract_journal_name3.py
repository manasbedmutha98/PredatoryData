import os
import pandas as pd
from difflib import get_close_matches
import shutil

HOME = "/home/kevinpatel711/temp_omics/" #temp_omics
LIST = "/home/kevinpatel711/omics_sub_jour_mapping/" #list of journal names
TARGET = "/home/kevinpatel711/omics_sub_wise/"

# df0 = pd.read_csv(LIST)
frames = os.listdir(LIST)

for frame in frames:
	print("Now executing ",frames)

	folder = frame[:-5]
	os.mkdir(TARGET+folder)

	df0 = pd.read_excel(LIST, sheet_name='Sheet1')
	names = df0['Journal Name'].values
	names = [name.lower().strip() for name in names]

	print("Journal names are", names)

	files = os.listdir(HOME)
	links = [file[:-4] for file in files]

	for link in links:
		name = get_close_matches(word=link, possibilities=names, n=1, cutoff=0.0)
		try:
			shutil.copy(LIST+link+".csv", TARGET+folder+"/"+link+".csv")
		except:
			print("Failure at ",folder, link, TARGET)



