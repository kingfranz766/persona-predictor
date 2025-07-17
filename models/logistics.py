import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load and clean data
df = pd.read_csv('datasets/personality_synthetic_dataset.csv')
df = df.dropna()

# Split features and labels
X = df.drop('personality_type', axis=1)
y = df['personality_type']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Cross-validate to check baseline model performance
logreg = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
cv_scores = cross_val_score(logreg, X_scaled, y, cv=5)

# Fit the final model
logreg.fit(X_train, y_train)

# Prediction function
def predict_with_confidence(input_df):
    input_scaled = scaler.transform(input_df)
    probs = logreg.predict_proba(input_scaled)[0]
    class_index = probs.argmax()
    return logreg.classes_[class_index], round(probs[class_index] * 100, 2)
