# Number Prediction using AI

A beginner-friendly Python project that trains a tiny machine learning model to predict the next number in a sequence.

**Internship:** Hex Softwares — Artificial Intelligence Internship
**Task:** 3 of 3

## About

This project demonstrates the core idea behind supervised learning: give a model examples (position → value), let it learn the underlying pattern, and use it to predict what comes next.

Example: given the sequence `1, 2, 3, 4, 5`, the model learns the pattern and predicts `6`.

## How It Works

1. The sequence is split into:
   - `X` — the position/index of each number (input)
   - `y` — the actual number at that position (label)
2. A `LinearRegression` model from scikit-learn is trained on this data.
3. The model predicts the value at the next position in the sequence.
4. The script also **explains its reasoning** — it prints the learned slope (step size), intercept (base value), and the full calculation used to arrive at the prediction, instead of just showing the final number.
5. The script also lets the user input their own custom sequence to test the model.

## Requirements

- Python 3.x
- scikit-learn
- numpy

Install dependencies:

```bash
pip install scikit-learn numpy
```

## Usage

Run the script:

```bash
python number_prediction.py
```

The script will:
1. Train on a sample sequence and print the predicted next number.
2. Prompt you to enter your own sequence (comma-separated) and predict its next value.

### Example

```
Sequence: [1, 2, 3, 4, 5, 6, 7, 8]
Detected pattern -> each step changes by approx: 1.00
Base value (intercept) -> 1.00
Formula learned: next_number ≈ (1.00 × position) + (1.00)
Position of next number: 8
Calculation: (1.00 × 8) + (1.00) = 9.00
Predicted next number: 9

--- Try your own sequence ---
Enter numbers separated by commas (e.g. 5,10,15,20): 5,10,15,20
Sequence: [5, 10, 15, 20]
Detected pattern -> each step changes by approx: 5.00
Base value (intercept) -> 5.00
Formula learned: next_number ≈ (5.00 × position) + (5.00)
Position of next number: 4
Calculation: (5.00 × 4) + (5.00) = 25.00
Predicted next number: 25
```

## Key Concepts Learned

- **Training vs. Prediction** — how a model fits data (`.fit()`) and then generates output (`.predict()`)
- **Feature/Label setup** — turning a simple sequence into an `X`/`y` format a model can learn from
- **Linear Regression** — a basic algorithm for learning numeric patterns
- **Model interpretability** — reading `coef_` (slope) and `intercept_` to explain *why* the model predicted a given value, not just what it predicted
- **User input handling** — parsing and validating comma-separated numeric input

## Author

Mahi — BS Artificial Intelligence, Hamdard University, Karachi