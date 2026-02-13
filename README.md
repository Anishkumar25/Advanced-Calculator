# 🧮 Python Scientific Calculator (CLI)

A command-line based scientific calculator built using Python.  
It performs arithmetic operations, scientific calculations, trigonometric functions, and maintains a persistent history file.

---

## 🚀 Features

### ➕ Basic Operations
- Addition
- Subtraction
- Multiplication
- Division
- Power

### 🔬 Scientific Functions
- Factorial
- Square Root
- Natural Logarithm (log)
- Trigonometric Functions:
  - sin
  - cos
  - tan
  - csc
  - sec
  - cot

### 📝 History Tracking
- Automatically saves every valid calculation
- Stores results in `history.txt`
- View complete history anytime from the menu

---

## 📂 Project Structure

```
calculator.py
history.txt (auto-created after first calculation)
README.md
```

- `calculator.py` → Main program
- `history.txt` → Stores calculation history
- `README.md` → Documentation

---

## ▶️ How to Run

### 1️⃣ Install Python
Make sure Python 3.x is installed.

Check version:
```
python --version
```

### 2️⃣ Run the Program
```
python calculator.py
```

The calculator menu will appear in the terminal.

---

## 🧠 How It Works

- Each operation is implemented as a separate function.
- Valid results are saved using the `save_history()` function.
- History is appended to `history.txt`.
- The calculator runs continuously until the user selects **Exit**.

---

## 📌 Important Notes

- Trigonometric functions accept angles in **radians**.
- Factorial accepts only **non-negative integers**.
- Division by zero is handled safely.
- Logarithm works only for **positive numbers**.

---

## 💻 Example Usage

```
Select operation:
1. Add
2. Subtract
...

Enter choice: 1
Enter first number: 10
Enter second number: 5
Result: 15
```

History file content:
```
10 + 5 = 15
```

---

## ⚠️ Limitations

- No GUI (command-line based only)
- History file grows indefinitely unless manually cleared
- Trigonometric functions use radians only

---

## 🔮 Possible Future Improvements

- Add degree-to-radian conversion
- Add GUI using Tkinter
- Add option to clear history
- Add better exception handling
- Support full expression input (e.g., `2 + 3 * 4`)

---

## 📜 License

Free to use for educational purposes.
