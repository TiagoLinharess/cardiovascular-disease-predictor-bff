from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class PreProcessor:

    def process(self, data, test_size, seed):
        # Separar as features e o target
        X = data.drop('num', axis=1)
        y = data['num']

        # Dividir o dataset em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)
        return (X_train, X_test, y_train, y_test)