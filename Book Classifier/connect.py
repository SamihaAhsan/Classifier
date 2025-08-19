import joblib
from flask import Flask, request  # you forgot to import request
from flask_cors import CORS


app = Flask(__name__)

CORS(app)
model = joblib.load("genre_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/connect", methods=['GET'])
def predict_genre():
    summary = request.args.get('summary') #treated as a string


    summary_converted = vectorizer.transform([summary])  # transform summary text
    genre_code = model.predict(summary_converted)[0]  # get predicted genre code

    if genre_code == 0:
        return "Romance"
    elif genre_code == 1:
        return "Mystery"
    elif genre_code == 2:
        return "Sci-fi"
    elif genre_code == 3:
        return "Western"
    elif genre_code == 4:
        return "Fiction"

if __name__ == '__main__':
    app.run(debug=True)
