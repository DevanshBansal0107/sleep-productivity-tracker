import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

def train_model():
    df = pd.read_csv("data/dataset.csv")

    X = df[["sleep_hours", "study_hours", "screen_time", "stress_level"]]
    y = df["productivity"]

    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)
    print("Model Accuracy (R2 Score):", round(r2_score(y, y_pred), 2))

    with open("models/trained_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved!")
