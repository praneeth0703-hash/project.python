# simple_ids.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Step 1: Create dummy network traffic data
# Features: [packet size, duration, number of connections]
# Labels: 0 = normal, 1 = attack
data = {
    'packet_size': [200, 500, 100, 700, 300, 50, 900, 120, 80, 1000],
    'duration':     [1, 3, 1, 4, 2, 0.5, 5, 0.7, 0.4, 6],
    'connections':  [10, 50, 5, 70, 20, 1, 90, 4, 2, 100],
    'label':        [0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)
X = df.drop('label', axis=1)
y = df['label']

# Step 2: Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 3: Evaluate model
y_pred = model.predict(X_test)
print("Evaluation:\n", classification_report(y_test, y_pred))

# Step 4: Test on new traffic sample
new_traffic = pd.DataFrame([[150, 1.2, 8]], columns=['packet_size', 'duration', 'connections'])
prediction = model.predict(new_traffic)

print("\nPrediction for new traffic:", "Attack 🚨" if prediction[0] == 1 else "Normal ✅")
