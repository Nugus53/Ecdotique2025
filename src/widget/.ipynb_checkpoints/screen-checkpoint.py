import ipywidgets as widgets
from ipywidgets import interactive
from functools import partial
import matplotlib.pyplot as plt

import sys
import os
sys.path.insert(0,  os.path.abspath(os.path.join(os.getcwd(), "../..")))
from corpora import achP,specificite

def ashMenu(data):
    import ipywidgets as widgets
    from IPython.display import display
    
    distance = widgets.Dropdown(
        description="distance :", 
        options=["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine", "dice", "euclidean", 
                 "hamming", "jaccard", "jensenshannon", "kulczynski1", "mahalanobis", "matching", "minkowski", 
                 "rogerstanimoto", "russellrao", "seuclidean", "sokalmichener", "sokalsneath", "sqeuclidean", "yule"],
        value="euclidean"
    )
    
    method = widgets.Dropdown(
        description="méthode :", 
        options=["single", "complete", "average", "weighted", "centroid", "median", "ward"], 
        value="ward"
    )
    
    nbclasse = widgets.IntText(description="nb classes :", value=3)
    button = widgets.Button(description='Run')
    out=widgets.Output()
    display(distance, method, nbclasse, button,out)

    def on_button_click(_):
        try:
            with out :
                achP(data=data, method=method.value, distance=distance.value, nbclasse=nbclasse.value)
        except Exception as e:
            print("Error in ACH.py")
            print(e)

    button.on_click(on_button_click)  # Pass function reference, not a cal

class Partition():
    def __init__(self,data):
        self.partitions=[]
        self.partition_count = 1 
        self.data=data
        self.out = widgets.Output()
        add_button = widgets.Button(description="Ajouter une partition")
        add_button.on_click(self.add_partition)

        self.method = widgets.Dropdown(
        description="méthode :", 
        options=["fisher", "chi2", "barnard"],
        value="barnard")
        
        calcul_button = widgets.Button(description="Calculer la spéficité")
        calcul_button.on_click(self.calcul_partition)
        
        display(add_button,calcul_button,self.method, self.out)
    
    def calcul_partition(self,_):
        rst=specificite(self.data, self.get_partitions(), self.method.value)
        rst.to_excel("export.xlsx")
        with self.out:
            display(rst)
        
    def add_partition(self,_):
        
    
        title = widgets.Label(f"Partition {self.partition_count}:")
        
        tags = widgets.TagsInput(
            value=[],
            allowed_tags=list(self.data.columns.tolist()),  
            allow_duplicates=False
        )
        
        partition_ui = widgets.VBox([title, tags])
        self.partitions.append(tags)
    
        with self.out:
            display(partition_ui)
    
        self.partition_count += 1  
        
    def get_partitions(self):
        partition_list = [tags.value for tags in self.partitions]  
        return partition_list 
    