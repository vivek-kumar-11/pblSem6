from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

model = joblib.load("model2.pkl")

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
    "exercise_minutes_per_week",
    "social_hours_per_week",
]

TARGET_COLUMNS = [
    "stress_level_0_10",
    "mental_wellness_index_0_100",
    "productivity_0_100"
]


@app.route("/", methods=["GET", "POST"])
def index():
    predictions = None
    error = None
    form_data = {}

    if request.method == "POST":
        try:
            work_screen_hours = float(request.form["work_screen_hours"])
            leisure_screen_hours = float(request.form["leisure_screen_hours"])

            form_data = {
                "age": float(request.form["age"]),
                "gender": request.form["gender"],
                "occupation": request.form["occupation"],
                "work_mode": request.form["work_mode"],
                "work_screen_hours": work_screen_hours,
                "leisure_screen_hours": leisure_screen_hours,
                "screen_time_hours": work_screen_hours + leisure_screen_hours,
                "sleep_hours": float(request.form["sleep_hours"]),
                "sleep_quality_1_5": float(request.form["sleep_quality_1_5"]),
                "exercise_minutes_per_week": float(request.form["exercise_minutes_per_week"]),
                "social_hours_per_week": float(request.form["social_hours_per_week"]),
            }

            input_df = pd.DataFrame([form_data])[FEATURE_COLUMNS]
            pred = model.predict(input_df)[0]

            predictions = {
                TARGET_COLUMNS[i]: round(float(pred[i]), 2)
                for i in range(len(TARGET_COLUMNS))
            }

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "index.html",
        predictions=predictions,
        error=error,
        form_data=form_data
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)