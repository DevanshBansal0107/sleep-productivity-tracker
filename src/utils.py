import pickle

def load_model():
    with open("models/trained_model.pkl", "rb") as f:
        return pickle.load(f)

def predict(model, sleep, study, screen, stress):
    return model.predict([[sleep, study, screen, stress]])[0]
