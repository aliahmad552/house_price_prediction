from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained pipeline model
model = pickle.load(open('lr.pkl', 'rb'))

# Load locations from CSV
locations_df = pd.read_csv('Cleaned_data.csv')
location_names = sorted(locations_df['location'].unique())

@app.route("/")
def index():
    return render_template("index.html", locations=location_names)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        location = request.form.get("location")
        total_sqft = float(request.form.get("total_sqft"))
        bath = int(request.form.get("bath"))
        bhk = int(request.form.get("bhk"))

        # Create DataFrame for prediction
        input_df = pd.DataFrame([[location, total_sqft, bath, bhk]],
                                columns=["location", "total_sqft", "bath", "bhk"])

        # Predict using model pipeline
        predicted_price = float(model.predict(input_df)[0])  # 👈 fixed here

        return jsonify({"price": round(predicted_price, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
