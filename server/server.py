import pickle
from flask import Flask, request, jsonify
import utils

app = Flask(__name__)



@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        squaremeters = float(request.form.get('total_sqft', 0))
        numberofrooms = int(request.form.get('rooms', 0))
        numprevowner = int(request.form.get('previousOwner', 1))
        floors = int(request.form.get('floors', 0))
        has_yard = request.form.get('hasyard') 
        has_pool =  request.form.get('haspool') 
        is_new_build =  request.form.get('build') 
        made=int(request.form.get('made'))
        ageofproperty=2024-made
        # # Nettoyage et conversion de 'build' en booléen puis en entier
        # isnewbuilt_str = request.form.get('build', 'false').strip().lower()
        # isnewbuilt = 1 if isnewbuilt_str == 'true' else 0
        

        estimated_price = utils.get_estimated_price(
            squaremeters=squaremeters,
            numberofrooms=numberofrooms,
            numprevowners=numprevowner,
            isnewbuilt=is_new_build,
            floors=floors,
            hasyard=has_yard,
            haspool=has_pool,
            made=made,
            ageofproperty=ageofproperty
        )

        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except ValueError as e:
        # Gestion des erreurs de conversion, log et retour d'une réponse adéquate
        print(f"Erreur de conversion : {e}")
        return jsonify({'error': 'Format de données invalide, veuillez vérifier vos entrées'}), 400
    except Exception as e:
        # Pour d'autres types d'erreurs
        print(f"Erreur rencontrée : {e}")
        return jsonify({'error': 'Une erreur est survenue lors du traitement de votre requête'}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    utils.load_saved_artifacts()
    app.run()


