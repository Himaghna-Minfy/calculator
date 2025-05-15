# calculator

🧮 Simple CLI Calculator
This is a simple command-line calculator written in Python. It allows users to perform basic arithmetic operations interactively, including addition, subtraction, multiplication, and division.

📌 Features
Interactive CLI-based interface

Supports the four basic operations:

1: Addition

2: Subtraction

3: Multiplication

4: Division

Handles invalid inputs gracefully

Allows continuous calculations using the result of the previous operation

Option to exit at any time by typing exit

💻 Usage
1. Run the program
bash
Copy
Edit
python calculator.py
2. Follow the prompts
Start by entering a number.

Select an operation:
1 (Addition), 2 (Subtraction), 3 (Multiplication), 4 (Division)

Enter the next number.

View the result and continue the operation, or type exit to quit.

🧠 Example
text
Copy
Edit
Simple CLI Calculator
Operations:
1: Addition
2: Subtraction
3: Multiplication
4: Division
Type 'exit' to quit
Enter a number: 10
Enter operation (1/2/3/4) or 'exit' to quit: 1
Enter next number: 5
Result: 15.0
Enter operation (1/2/3/4) or 'exit' to quit: 3
Enter next number: 2
Result: 30.0
⚠️ Input Validation
Non-numeric inputs are rejected with an appropriate message.

Division by zero is prevented with an error message:
"Error! Division by zero is not allowed"

🛠️ Requirements
Python 3.x

📂 File Structure
bash
Copy
Edit
calculator.py       # Main Python script containing the calculator logic
README.md           # Project documentation
