import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
plt.style.use('seaborn-paper')

# Grab the data from the data directory
df = pd.read_csv("../3_data/data.csv")

# How to make a marker dictionary
markers = ['s','o','^','d']
method_markers={}
for method, marker in zip(set(df['method']),markers):
    method_markers[method] = marker

# Some nice settings for error bar plots
errkws = {'mec':'k',
          'mew':1,
          'capsize':2 } 

# Make the figure size the same as the column width. You will not 
# resize the figure.
fig = plt.figure(figsize=(3.5,3))

#While Seaborn is good for quick plots, I usually just use matplotlib 
# directly for good control
for method, grp in df.groupby("method"):
    plt.errorbar('position','energy','error', data = grp, label=method, marker=method_markers[method], **errkws)
plt.xlabel("Position (Bohr)")
plt.ylabel("Energy (Hartree)")
plt.legend(loc='best')
sns.despine()
plt.savefig("fig_usefulname.pdf",bbox_inches='tight')