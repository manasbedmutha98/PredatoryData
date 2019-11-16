import os
import pandas as pd
from difflib import get_close_matches
import shutil

HOME = "/home/manas/Semester VII/Natural Language Processing/Project/"
LIST = "/home/manas/Semester VII/Natural Language Processing/Project/omicsbiomednames.csv"
TARGET = ""


names = df0['Journal Name'].values
names = [name.lower().strip() for name in names]

print(names)

files = os.listdir(HOME)

links = [file[:-5] for file in files]

# https://www.omicsonline.org/archive-advances-in-crop-science-and-technology-open-access.php
for i,link in enumerate(links):
	# if i==0:
	# 	continue

	# link = link.replace("-open-access.php","")
	# link = link.replace(".php","")
	# link = link.replace("https://www.omicsonline.org/archive-","")
	#link = " ".join(link.split("-"))
	
	# print(link)
	# if link in names:
	# 	print(i-1,link)

	name = get_close_matches(word=link, possibilities=names, n=1, cutoff=0.0)
	shutil.copy(LIST+link+".csv", TARGET)



import os
import pandas as pd
from difflib import get_close_matches
import shutil

HOME = "/home/kevinpatel711/temp_omics/" #temp_omics
LIST = "/home/kevinpatel711/omics_sub_jour_mapping/"
TARGET = "/home/kevinpatel711/"

# df0 = pd.read_csv(LIST)
df0 = pd.read_excel(LIST, sheet_name='Sheet1')
names = df0['Journal Name'].values
names = [name.lower().strip() for name in names]

print(names)

files = os.listdir(HOME)

links = [file[:-4] for file in files]

# https://www.omicsonline.org/archive-advances-in-crop-science-and-technology-open-access.php
for i,link in enumerate(links):
# if i==0:
# continue

# link = link.replace("-open-access.php","")
# link = link.replace(".php","")
# link = link.replace("https://www.omicsonline.org/archive-","")
#link = " ".join(link.split("-"))

# print(link)
# if link in names:
# print(i-1,link)

name = get_close_matches(word=link, possibilities=names, n=1, cutoff=0.0)
shutil.copy(LIST+link+".csv", TARGET)



