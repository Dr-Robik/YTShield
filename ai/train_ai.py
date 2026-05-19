import pandas as pd
import glob
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle

files = glob.glob("../data/Youtube*.csv")  
dfs = []

for file in files:
    df = pd.read_csv(file)
    df = df.rename(columns={'CONTENT': 'comment', 'CLASS': 'label'})
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)
print(f"[INFO] Combined dataset shape: {data.shape}")
print(data['label'].value_counts())

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)        
    text = re.sub(r'[^a-z0-9\s]', '', text)   
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

data['comment'] = data['comment'].apply(clean_text)

X = data['comment']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)


y_pred = model.predict(X_test_vec)
print("\n[INFO] Classification Report:")
print(classification_report(y_test, y_pred))

pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("\n[INFO] Model and vectorizer saved in ./ai/")
