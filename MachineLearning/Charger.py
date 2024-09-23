import pandas as pd

class Charger: 

    def loadData(self):
        # Carregar o dataset diretamente de uma URL
        url = "https://raw.githubusercontent.com/carlosfab/curso_data_science_na_pratica/master/modulo_03/heart-disease-uci.csv"
        return pd.read_csv(url, delimiter=',')