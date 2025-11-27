from tree import DecisionTreeManual

model = DecisionTreeManual()

test3 = {
    "Age": ">35",
    "Income": "Medium",
    "Gender": "Female",
    "Ms": "Married"
}

print("Q6 Decision:", model.predict(test3))