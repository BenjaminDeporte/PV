# Quelques utilitaires pour faire simulations

# imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------

class Productible():
    """class de base pour importer un fichier hourly de PV Watts, et sortir des data utilisables par le modèle
    """
    
    def __init__(self, filename:str) -> None:
        """le constructeur prend en argument un fichier *.csv issu de PVWatts

        Args:
            filename (str): nom du fichier *.csv utilisé pour instancier l'objet
        """
        
        STARTING_ROW = 14
        
        with open(filename, "r", encoding="utf-8") as f:
            df = pd.read_csv(f, 
                             header=STARTING_ROW,
                             nrows=8760
                             )
            self.df = df
            
    def get_df(self):
        """retourne la df
        """
        return self.df
    
    def get_hourly(self, month, day, hour):
        """renvoie la production AC horaire au temps (month, day, jour)

        Args:
            month (int): mois
            day (int): jour
            hour (int): heure
        """
        
        filter1 = (self.df['Month'] == month)
        filter2 = (self.df['Day'] == day)
        filter3 = (self.df['Hour'] == hour)
        
        return float(self.df[filter1][filter2][filter3]['AC System Output (W)'])