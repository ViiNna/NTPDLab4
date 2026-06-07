from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression
import numpy as np
from waitress import serve

#ZADANIE 1

# Utworzenie nowej instancji flask
app = Flask(__name__)

#Mapowanie endpointu '/'
@app.route("/")
def home():
    return jsonify({"message": "Hello World"})

#app.run(host="127.0.0.1", port=8000)


#ZADANIE 2

#Przygotowanie przykładowych danych
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([2, 4, 6, 8, 10])

#Trenowanie modelu
model = LinearRegression()
model.fit(X_train, y_train)

# #Utworzenie endpointu do otrzymywania predykcji
# @app.route("/predict", methods=["POST"])
# def predict():
#     #Pobieranie danych z zapytania
#     data = request.get_json()
#     #Pobieranie inputu do modelu
#     value = np.array([[data["value"]]])
#     #Wykonanie predykcji na danych
#     prediction = model.predict(value)
#     #Zwrócenie otrzymanej predykcji
#     return jsonify({"prediction": prediction.tolist()})



#ZADANIE 3

#Utworzenie endpointu do otrzymywania predykcji
@app.route("/predict", methods=["POST"])
def predict():
    #Pobieranie danych z zapytania
    data = request.get_json()

    #Obsługa braku  JSONa
    if data is None:
        return jsonify({"error": "Brak danych JSON w zapytaniu"}), 400

    #Obsługa braku wartości value w zapytaniu
    if "value" not in data:
        return jsonify({"error": "Brak pola value"}), 400

    #Pobieranie inputu do modelu
    value = np.array([[data["value"]]])
    #Wykonanie predykcji na danych
    prediction = model.predict(value)
    #Zwrócenie otrzymanej predykcji
    return jsonify({"prediction": prediction.tolist()})



#ZADANIE 4

#endopint "/info" zawierający informacje o mopdelu
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "model_type": "LinearRegression",
        "num_features": 1,
        "description": "Dane tego modelu są liczbami."
    })

#endpoint "/health", który informuje czy serwej jest w trybie online
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})



#ZADANIE 5

#Uruchomienie aplikacji w trybie produkcyjnym z użyciem Waitress
serve(app, host="0.0.0.0", port = 8000)