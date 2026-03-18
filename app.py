from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("house_model.pkl", "rb"))

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            int(request.form.get('area', 1000)),
            int(request.form.get('bedrooms', 2)),
            int(request.form.get('bathrooms', 2)),
            int(request.form.get('floors', 1)),
            int(request.form.get('parking', 1)),
            int(request.form.get('location_score', 5)),
            int(request.form.get('nearby_hospitals', 1)),
            int(request.form.get('furnished', 0)),
            int(request.form.get('material_quality', 5)),
            int(request.form.get('location_type', 0))
        ]

        prediction = model.predict([features])

        return render_template(
            "index.html",
            prediction_text=f"Estimated Price: ₹{int(prediction[0])}"
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")


# YE LAST ME HOGA (IMPORTANT)
if __name__ == "__main__":
    app.run(debug=True)