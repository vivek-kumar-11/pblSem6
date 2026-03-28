from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load trained pipeline
model = joblib.load("model.pkl")

FEATURE_COLUMNS = [
    "age",
    "gender",
    "occupation",
    "work_mode",
    "screen_time_hours",
    "work_screen_hours",
    "leisure_screen_hours",
    "sleep_hours",
    "sleep_quality_1_5",
    "stress_level_0_10",
    "exercise_minutes_per_week",
    "social_hours_per_week",
]

def estimate_prediction_range(input_df):
    """
    Estimate uncertainty for Random Forest regression using variation
    among predictions from individual trees.
    """
    try:
        preprocessor = model.named_steps["preprocessor"]
        rf_model = model.named_steps["model"]

        transformed = preprocessor.transform(input_df)
        tree_preds = np.array([tree.predict(transformed)[0] for tree in rf_model.estimators_])

        mean_pred = np.mean(tree_preds)
        std_pred = np.std(tree_preds)

        lower = round(mean_pred - std_pred, 2)
        upper = round(mean_pred + std_pred, 2)

        return round(std_pred, 2), lower, upper
    except Exception:
        return None, None, None
        
    try:
        preprocessor = model.named_steps["preprocessor"]
        rf_model = model.named_steps["model"]

        transformed = preprocessor.transform(input_df)

        tree_preds = np.array([tree.predict(transformed)[0] for tree in rf_model.estimators_])
        pred_std = np.std(tree_preds)

        # Convert std into a simple confidence score
        # Lower std => higher confidence
        confidence = max(0, min(100, 100 - (pred_std * 12)))
        return round(confidence, 2), round(pred_std, 2)
    except Exception:
        return None, None

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    uncertainty = None
    lower_range = None
    upper_range = None
    error = None
    form_data = {}

    if request.method == "POST":
        try:
            form_data = {
                "age": float(request.form["age"]),
                "gender": request.form["gender"],
                "occupation": request.form["occupation"],
                "work_mode": request.form["work_mode"],
                "screen_time_hours": float(request.form["screen_time_hours"]),
                "work_screen_hours": float(request.form["work_screen_hours"]),
                "leisure_screen_hours": float(request.form["leisure_screen_hours"]),
                "sleep_hours": float(request.form["sleep_hours"]),
                "sleep_quality_1_5": float(request.form["sleep_quality_1_5"]),
                "stress_level_0_10": float(request.form["stress_level_0_10"]),
                "exercise_minutes_per_week": float(request.form["exercise_minutes_per_week"]),
                "social_hours_per_week": float(request.form["social_hours_per_week"]),
            }

            input_df = pd.DataFrame([form_data], columns=FEATURE_COLUMNS)
            pred = model.predict(input_df)[0]
            prediction = round(float(pred), 2)

            uncertainty, lower_range, upper_range = estimate_prediction_range(input_df)
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
    "index.html",
    prediction=prediction,
    uncertainty=uncertainty,
    lower_range=lower_range,
    upper_range=upper_range,
    error=error,
    form_data=form_data
)

if __name__ == "__main__":
    app.run(debug=True)