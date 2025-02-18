from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import numpy as np
import sys
import os

sys.path.insert(0,  os.path.abspath(os.path.join(os.getcwd(), "../..")))
import matplotlib.pyplot as plt




def achP(data,method,distance,nbclasse):
      try :
        plt.figure(figsize=(8, 3),dpi=150)
        hierarchy.set_link_color_palette(['blue', 'red', 'orange', 'green','pink','purple'])
        Z = linkage(data,method=method,metric=distance)
        last = Z[-10:, 2]
        last_rev = last[::-1]
        idxs = np.arange(2, len(last) + 2)

        hierarchy.dendrogram(Z,orientation='top',count_sort='ascending',distance_sort='ascending',labels=data.index,color_threshold=last_rev[np.where(idxs==nbclasse)],above_threshold_color='black',leaf_font_size=5)
        plt.show()
      except Exception as e:
       print("Axh.py")
       print(e)
