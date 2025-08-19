import pandas as pd # used to manipulate csv data
from sklearn.feature_extraction.text import CountVectorizer #converts text in csv to tokens to count the number of each word
from sklearn.model_selection import train_test_split #split data, some for training, some for testing
from sklearn.naive_bayes import MultinomialNB #classifier, classifying to genre baed on word count
from sklearn.metrics import accuracy_score #accuracy of its predictions
# pip means to install python package everywhere, import is to import to specific file
import joblib
reading = pd.read_csv('cleaned_data.csv') #reading now stores the dataframe
reading['Genre'] = reading['Genre'].map({'Romance': 0, 'Mystery': 1, 'Sci-fi': 2, 'Western': 3, 'Fiction': 4}) #assigning numbers to each thing
 #splitting the data
X=reading['Summary']
y = reading['Genre']
# assigning to each variable the x and y test and train values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) #testing is 30%

vectorizer = CountVectorizer() # is an object now vectorizer is storing a count vectorizer object, converting text data to numerical values
X_train_vectors = vectorizer.fit_transform(X_train) #fit_transform owned by vectorizer object (function only useable on vectorizer ALL DATATYPES ARE OBJECTS) anyways it LETS MODEL LEARN VOCABULARY ITS LOOKIN FOR
X_test_vectors = vectorizer.transform(X_test)

model = MultinomialNB() #model is an object (an instance) of the class MultinomialNB.
model.fit(X_train_vectors, y_train)
y_pred = model.predict(X_test_vectors)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%\n") #outputs to stdout(terminal)
joblib.dump(model, 'genre_model.pkl')

joblib.dump(vectorizer, 'vectorizer.pkl')
