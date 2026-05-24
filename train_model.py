from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

# Sample dataset
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
scores = np.array([35, 40, 50, 55, 65, 70, 80, 90])

# Train model
model = LinearRegression()
model.fit(hours, scores)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
import os
print("Saving in:", os.getcwd())