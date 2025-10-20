from tkinter import *
from random import randint, choice


root = Tk()
root.geometry('550x550')
root.title('Online Quiz')

givenAnswer = StringVar()
score = 0
questionCount = 0
totalQuestions = 5
time_left = 10
Answer = 0



def generateQuestion():

    global Answer, questionCount, time_left

    if questionCount >= totalQuestions:
        endQuiz()
        return

    # Reset timer
    time_left = 10
    countdown()

    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = choice(['+', '-', '*', '/'])

    if operator == '+':
        Answer = number1 + number2
    elif operator == '-':
        Answer = number1 - number2
    elif operator == '*':
        Answer = number1 * number2
    elif operator == '/':
        Answer = round(number1 / number2, 2)

    Question = f"{number1} {operator} {number2}"
    QuestionLabel.config(text=Question)
    resultLabel.config(text="")
    givenAnswer.set("")

def checkAnswer():

    global score, questionCount
    try:
        userAnswer = float(givenAnswer.get())
        if abs(userAnswer - Answer) < 0.01:
            resultLabel.config(text=" Correct!", fg="green")
            score += 1
        else:
            resultLabel.config(text=f"Wrong! Correct: {Answer}", fg="red")

        questionCount += 1
        scoreLabel.config(text=f"Score: {score}")
    except:
        resultLabel.config(text="Please enter a number", fg="orange")

def countdown():

    global time_left, questionCount

    if time_left > 0:
        timeLabel.config(text=f" Time Left: {time_left}s")
        time_left -= 1
        root.after(1000, countdown)
    else:
        resultLabel.config(text=" Time Over!", fg="red")
        questionCount += 1
        generateQuestion()

def endQuiz():

    QuestionLabel.config(text="Quiz Finished!!!")
    resultLabel.config(text=f" Final Score: {score}/{totalQuestions}", fg="blue")
    AnswerEntry.config(state=DISABLED)
    SubmitButton.config(state=DISABLED)
    NextButton.config(state=DISABLED)
    RestartButton.grid(row=6, column=0, columnspan=2, pady=10)

def restartQuiz():

    global score, questionCount
    score = 0
    questionCount = 0
    scoreLabel.config(text=f"Score: {score}")
    AnswerEntry.config(state=NORMAL)
    SubmitButton.config(state=NORMAL)
    NextButton.config(state=NORMAL)
    RestartButton.grid_forget()
    generateQuestion()
headingLabel = Label(root, text=' Online Quiz', font=('Comic Sans MS', 24, 'bold'), bg="#f2f2f2", fg="#333")
headingLabel.grid(row=0, column=0, columnspan=2, pady=20)

QuestionLabel = Label(root, text="", font=('Calibri', 22), bg="white", width=20, height=2, relief="ridge")
QuestionLabel.grid(row=1, column=0, columnspan=2, pady=20)

AnswerEntry = Entry(root, textvariable=givenAnswer, font=('Arial', 20), width=10, justify='center')
AnswerEntry.grid(row=2, column=0, pady=10)

SubmitButton = Button(root, text='Submit', font=('Arial', 18), bg="#0078D7", fg="white",
                      command=checkAnswer, width=8)
SubmitButton.grid(row=2, column=1, padx=10)

NextButton = Button(root, text='Next', font=('Arial', 18), bg="#28a745", fg="white",
                    command=generateQuestion, width=8)
NextButton.grid(row=3, column=1, pady=10)

resultLabel = Label(root, text="", font=('Arial', 16), bg="#f2f2f2")
resultLabel.grid(row=4, column=0, columnspan=2, pady=20)

scoreLabel = Label(root, text=f"Score: {score}", font=('Arial', 16, 'bold'), bg="#f2f2f2", fg="blue")
scoreLabel.grid(row=5, column=0, pady=10)

timeLabel = Label(root, text=f"Time Left: {time_left}s", font=('Arial', 14), bg="#f2f2f2", fg="red")
timeLabel.grid(row=5, column=1, pady=10)

RestartButton = Button(root, text='Restart', font=('Arial', 18), bg="#ff9900", fg="white",
                       command=restartQuiz, width=10)
generateQuestion()

root.mainloop()
