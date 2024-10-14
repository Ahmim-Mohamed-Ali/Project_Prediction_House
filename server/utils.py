import json
import pickle
import numpy as np
import default_values as dv
__locations = None
__data_columns = None
__model = None

def get_estimated_price(**kwargs):
    # Créez un tableau de zéros avec la longueur des colonnes de données
    x = np.zeros(len(__data_columns))
    
    # Remplir les valeurs pour les caractéristiques fournies ou par défaut
    for i, feature in enumerate(__data_columns):
        # Utiliser kwargs pour obtenir la valeur ou la valeur par défaut
        x[i] = kwargs.get(feature, dv.default_values[feature])
    # Prédire le prix en utilisant le modèle
    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns


    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']


    global __model
    if __model is None:
        with open('./artifacts/paris_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")



def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price(squaremeters=60000, floors=3))