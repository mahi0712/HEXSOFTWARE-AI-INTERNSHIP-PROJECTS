
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_with_reasoning(sequence):
    X = np.array(range(len(sequence))).reshape(-1, 1)
    y = np.array(sequence)

    model = LinearRegression()
    model.fit(X, y)

    slope = model.coef_[0]        # m -> pattern ka "step" (har baar kitna badha)
    intercept = model.intercept_  # c -> starting point

    next_index = np.array([[len(sequence)]])
    prediction = model.predict(next_index)[0]

    # ---- REASONING / EXPLANATION ----
    print(f"\nSequence: {sequence}")
    print(f"Detected pattern -> each step changes by approx: {slope:.2f}")
    print(f"Base value (intercept) -> {intercept:.2f}")
    print(f"Formula learned: next_number ≈ ({slope:.2f} × position) + ({intercept:.2f})")
    print(f"Position of next number: {len(sequence)}")
    print(f"Calculation: ({slope:.2f} × {len(sequence)}) + ({intercept:.2f}) = {prediction:.2f}")
    print(f"Predicted next number: {round(prediction)}")

    return round(prediction)


# ---- Run on sample sequence ----
sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
predict_with_reasoning(sample_sequence)

# ---- Let user try their own ----
print("\n--- Try your own sequence ---")
user_input = input("Enter numbers separated by commas (e.g. 5,10,15,20): ")
user_seq = [int(x.strip()) for x in user_input.split(",")]

predict_with_reasoning(user_seq)