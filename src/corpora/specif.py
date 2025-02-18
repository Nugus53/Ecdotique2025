import pandas as pd
import numpy as np
from scipy.stats import fisher_exact, barnard_exact, chi2_contingency

def specificite(df, partitions, mode):
    # Vérifier si les partitions existent dans df

    selected_columns = [group for group in partitions if all(col in df.columns for col in group)]
    
    if not selected_columns:
        raise ValueError("Aucune colonne valide dans les partitions sélectionnées.")
    
    # Création d'un DataFrame avec les sommes par partition
    new_df = pd.DataFrame({
        str(idx+1): df.loc[:, group].sum(axis=1) for idx, group in enumerate(selected_columns)
    })


    df = new_df
    matrice = df.copy()
    total_sum = df.to_numpy().sum()

    for mot in df.index:
        for part in df.columns:
            freq_courante = df.loc[mot, part]
            sum_freq_mot_autres = df.loc[mot, :].sum() - freq_courante
            sum_freq_partition_sans_mot = df[part].sum() - freq_courante
            sum_freq_autres_sans_mot = total_sum - (sum_freq_mot_autres + sum_freq_partition_sans_mot + freq_courante)
    
            contingency_table = [[freq_courante, sum_freq_mot_autres], 
                                 [sum_freq_partition_sans_mot, sum_freq_autres_sans_mot]]
            
            match mode:
                case 'fisher':
                    value = fisher_exact(contingency_table)[1]
                    matrice.loc[mot, part] = 1-float(value)
                case 'chi2':
                    value = chi2_contingency(contingency_table)[1]
                    matrice.loc[mot, part] = 1-float(value)
                case 'barnard':
                    value = barnard_exact(contingency_table).pvalue
                    matrice.loc[mot, part] = float(value)
          
    return matrice

'''
partition_list = get_partitions() # Transformation en liste plate
result_matrix = spécificite(value.transpose(), partition_list, 'barnard')

# Trier par la première partition (colonne '1')
sorted_result = result_matrix.sort_values(by='1', ascending=False)

sorted_result.to_excel("export.xlsx")
'''
