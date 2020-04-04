# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:20:41 2020

@author: clems
"""

#Packages
from Embedding import Embedding
from Extracting import Extracting

# Files
filename_covert = "Declaration_of_Independance.txt"
filename_overt = "ballons_rgb.bmp"
filename_dirty = "LSBFile.bmp"
filename_extracted = "extracted_file.txt"

# Embedding
embed = Embedding(filename_covert,filename_overt,filename_dirty)
embed.embedding_process()

#Extracting
extract = Extracting(filename_dirty,filename_extracted)
extract.extracting_process()