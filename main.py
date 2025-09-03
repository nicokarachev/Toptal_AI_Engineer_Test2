import pandas as pd
from sklearn.model_selection import train_test_split
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


def simple_tokenizer(text):
    # Replace emails and Twitter handles
    text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', 'E_MAIL', text)
    text = re.sub(r'@\w+', 'TWITTER', text)
    
    # Handle complex punctuation first
    text = re.sub(r'\!\?\b', 'EXCLAM_QUESTION', text)
    text = re.sub(r'\!\!\!+', 'STRONG_EXCLAM', text)
    
    # Replace basic punctuation
    punct_mapping = {
        '!': 'EXCLAMATION',
        '?': 'QUESTION',
        ',': 'COMMA',
        '\.': 'DOT',
        '\.\.\.': 'ELLIPSIS',
        ';': 'SEMICOLON',
        ':': 'COLON'
    }
    
    # Handle ellipsis first
    text = re.sub(r'\.\.\.', 'ELLIPSIS', text)
    
    for p, token in punct_mapping.items():
        text = re.sub(r'(?<!\w)'+p+'(?!\w)', f' {token} ', text)
    
    # Split by whitespace
    tokens = text.split()
    return tokens


# Load dataset
df = pd.read_csv("language.csv")  # columns: 'text', 'language'

# Split dataset: 80% train, 20% test
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['language'])

# Create a pipeline: TF-IDF + Logistic Regression
model = Pipeline([
    ('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(1,3))),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train
model.fit(train_df['text'], train_df['language'])

# Predict
preds = model.predict(test_df['text'])

# Accuracy
acc = accuracy_score(test_df['language'], preds)
print("Test accuracy:", acc)