class DecisionTreeManual:
    def __init__(self):
        self.tree = {
            "Age": {
                "<21": {
                    "Gender": {
                        "Male": "No",
                        "Female": "Yes"
                    }
                },
                "21-35": "Yes",
                ">35": {
                    "Ms": {
                        "Single": "Yes",
                        "Married": "No"
                    }
                }
            }
        }

    def predict(self, sample: dict):
        node = self.tree
        while isinstance(node, dict):
            feature = next(iter(node))
            value = sample.get(feature)

            if value not in node[feature]:
                raise ValueError(f"Value '{value}' not found for '{feature}'")

            node = node[feature][value]

        return node