from flask import Flask, request, render_template 
import joblib
import mysql.connector


app = Flask(__name__)


model = joblib.load("genre_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

db = mysql.connector.connect(
    host="localhost",       
    user="me",       
    database="bookgen",    
    use_pure=True
)

@app.route("/connect", methods=['GET'])



def predict_genre():
    summary = request.args.get('summary') #treated as a string
    if summary:

        summary_converted = vectorizer.transform([summary])  # transform summary text
        genre_code = model.predict(summary_converted)[0]  # get predicted genre code

        if genre_code == 0:
            return render_template("front.html", msg="Romance")
        elif genre_code == 1:
            return render_template("front.html", msg="Mystery")
        elif genre_code == 2:
            return render_template("front.html", msg="Sci-Fi")
        elif genre_code == 3:
            return render_template("front.html", msg="Western")
        elif genre_code == 4:
            return render_template("front.html", msg="Fiction")

    return render_template("front.html", msg=None)
if __name__ == '__main__':
    app.run(debug=True)
