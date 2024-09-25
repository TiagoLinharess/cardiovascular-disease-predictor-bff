import pandas as pd

class Charger: 

    def loadData(self):
        # Carregar o dataset diretamente de uma URL
        url = "./MachineLearning/data/heart-disease-uci.csv"
        return pd.read_csv(url, delimiter=',')