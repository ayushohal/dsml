import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Step 1: Load dataset
df = pd.read_csv("Decision.csv")

print("=== Dataset Preview ===")
print(df.head())

if "Id" in df.columns:
    df = df.drop(columns=["Id"])

# Step 2: Convert categorical data to numeric using LabelEncoder
le = LabelEncoder()
encoded_df = df.apply(le.fit_transform)

# Step 3: Split features (X) and target/output variable (y)
# MAKE SURE your dataset has a column named "Buys" or modify accordingly.
X = encoded_df.drop("Buys", axis=1)
y = encoded_df["Buys"]

# Step 4: Train the decision tree model
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# Step 5: Prepare test data for prediction
# Original test data:
# Age <21, Income Low, Gender Female, Marital Status Married

test_data = pd.DataFrame({
    "Age": ["<21"],
    "Income": ["Low"],
    "Gender": ["Female"],
    "Ms": ["Married"]
})

# Encode test data using the same label encoders
for i, col in enumerate(test_data.columns):
    test_data[col] = le.fit(df[col]).transform(test_data[col])

# Step 6: Predict
prediction = model.predict(test_data)[0]

# Step 7: Decode prediction back to original label
final_decision = le.fit(df["Buys"]).inverse_transform([prediction])[0]

print("\n=== Final Prediction for Test Data ===")
print("Predicted Decision:", final_decision)
