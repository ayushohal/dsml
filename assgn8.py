from tree import DecisionTreeManual

model = DecisionTreeManual()

test4 = {
    "Age": "21-35",
    "Income": "Low",
    "Gender": "Male",
    "Ms": "Married"
}

print("Q7 Decision:", model.predict(test4))