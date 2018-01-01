#-*- coding:utf-8 –*-
from matplotlib import font_manager as fm
from  matplotlib import cm

import matplotlib as mpl

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

shapes = ['Cross', 'Cone', 'Egg', 'Teardrop', 'Chevron', 'Diamond', 'Cylinder',

       'Rectangle', 'Flash', 'Cigar', 'Changing', 'Formation', 'Oval', 'Disk',

       'Sphere', 'Fireball', 'Triangle', 'Circle', 'Light']

values = [287, 383, 842, 866, 1187, 1405, 1495, 1620, 1717, 2313, 2378, 3070, 4332, 5841, 6482, 7785, 9358, 9818, 20254]

s = pd.Series(values, index=shapes)

labels = s.index

sizes = s.values


explode = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)  # only "explode" the 1st slice

fig1, axes = plt.subplots()

ax1, ax2 = axes.ravel()

patches, texts, p_text = ax1.pie(sizes, explode=explode, labels=labels, autopct = '%3.1f%%', shadow=False,
                                 startangle=90, labeldistance = 1.2, pctdistance = 0.8)

#patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
#                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
#                                startangle = 90,pctdistance = 0.6)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

proptease = fm.FontProperties()

proptease.set_size('xx-small')

plt.setp(p_text, fontproperties=proptease)

plt.setp(texts, fontproperties=proptease)
ax1.set_title('Shapes', loc='center')
ax2.axis('off')
ax2.legend(patches, labels, loc='center left')
plt.tight_layout()

#plt.savefig('Demo_project_set_font.jpg')
#ax1.legend(labels, loc=2)

plt.show()