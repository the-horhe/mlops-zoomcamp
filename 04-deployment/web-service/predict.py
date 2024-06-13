import pickle
from sklearn.feature_extraction._dict_vectorizer import DictVectorizer
from sklearn.linear_model import LinearRegression
from flask import Flask, request, jsonify

with open("lin_reg.bin", "rb") as f:
    (dv, model) = pickle.load(f)

assert isinstance(dv, DictVectorizer)
assert isinstance(model, LinearRegression)

def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)

    return preds[0]

app = Flask("duration-prediction")

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    ride = request.get_json()
    pred = predict(ride)

    result = {
        "duration": pred
    }

    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
