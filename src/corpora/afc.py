from fanalysis.ca import CA
import matplotlib.pyplot as plt

def afc(D):
    afc = CA(row_labels=D.index,col_labels=D.columns)
    afc.fit(D.values)
    fig, ax = plt.subplots(figsize=(10,10))
    for i in range(D.shape[0]):
        ax.text(afc.row_coord_[i,0],afc.row_coord_[i,1],D.index[i],color='blue')
    #modalités colonne
    for i in range(D.shape[1]):
        ax.text(afc.col_coord_[i,0],afc.col_coord_[i,1],D.columns[i],color='red')
    plt.show()