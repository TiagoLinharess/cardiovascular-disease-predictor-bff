import pandas as pd

class Charger: 

    def loadData(self, url):
        # Carregar o dataset diretamente de uma URL
        return pd.read_csv(url, delimiter=',')