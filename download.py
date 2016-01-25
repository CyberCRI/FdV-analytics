# -*- coding: utf-8 -*-

from pubmed2wos import WOS

import pandas as pd
import os

#WOS(query="AU=(HO WAN kevin)", outfile="test")

phd = pd.read_csv("sources/phd.csv")

for idx, student in phd.iterrows():
  last_name = student[0]
  first_name = student[1]
  promotion = student[2]

  if not os.path.isdir("refs/"+promotion):
    os.makedirs("refs/"+promotion)

  if not os.path.exists("refs/"+promotion+"/"+last_name.lower()+".tsv"):
    WOS(query='AU=('+last_name.decode('utf-8')+' '+first_name.decode('utf-8')+')',outfile="refs/"+promotion+"/"+last_name.lower())
