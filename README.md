🧮 Online Quiz (Tkinter Python App)
📘 Overview

The Online Quiz is a simple interactive desktop application built with Python’s Tkinter library.
It generates random arithmetic questions (+, -, *, /) and tests the user’s calculation skills under a time limit.
The quiz keeps track of the user’s score, displays real-time countdowns, and allows restarting after completion.

🎯 Features

✅ Random arithmetic question generation
✅ Live countdown timer for each question
✅ Automatic score tracking
✅ Real-time feedback (Correct/Wrong)
✅ Restart functionality after quiz completion
✅ Simple and clean Tkinter interface

🧩 How It Works

When the app starts, a random math question is displayed.

The user enters their answer and clicks Submit.

If correct, they earn 1 point; otherwise, the correct answer is shown.

The user has 10 seconds to answer each question.

After 5 questions, the quiz ends and shows the final score.

The user can restart the quiz anytime.

🖥️ Interface Layout
Element	Description
Question Label	Displays the current arithmetic question
Entry Box	User types their answer here
Submit Button	Checks the entered answer
Next Button	Moves to the next question
Score Label	Shows current score
Time Label	Displays countdown timer
Restart Button	Restarts the entire quiz
⚙️ Requirements

Python 3.8+

Tkinter (comes pre-installed with Python)

▶️ Run the Program
# Step 1: Clone the repository
git clone https://github.com/your-username/online-quiz.git

# Step 2: Navigate to project folder
cd online-quiz

# Step 3: Run the program
python onlinequize.py

🧠 Code Structure
Function	Purpose
generateQuestion()	Generates random math problems
checkAnswer()	Verifies user's input and updates score
countdown()	Runs the 10-second timer for each question
endQuiz()	Displays final score and disables inputs
restartQuiz()	Resets game variables to start again
📸 Example UI
------------------------------
|      🧮 Online Quiz        |
|  5 + 7 = ?                 |
|  [ Your Answer:  12 ]      |
|  [Submit]   [Next]         |
|  Score: 1   Time: 8s       |
------------------------------

🏁 Future Improvements

Add difficulty levels (easy, medium, hard)

Add category selection (math, general knowledge)

Store scores in a local database

Include leaderboard functionality

Project 2: Problem Solve Notebook (probnlemsolve.ipynb)
🧠 Overview

This Jupyter Notebook contains different Python coding exercises and logical problem-solving examples.
It is designed for beginners to practice Python functions, loops, and algorithms interactively.

🧰 Contents

Basic Python syntax and logic problems

List and loop practice

Function-based problem-solving

Examples with outputs

▶️ Run Instructions

Install Jupyter Notebook:

pip install notebook


Open the notebook:

jupyter notebook probnlemsolve.ipynb


Run each cell to see results.

🎯 Purpose

Strengthen problem-solving skills

Learn Python programming step by step

Prepare for programming lab or viva

📜 License

This project is open-source under the MIT License.
