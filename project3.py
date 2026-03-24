#make A quiz game 
import random
def Quiz_Game():
    Questions = ["What is the capital of France?",
                 "What is 2 + 2?",
                 "What is the largest planet in our solar system?",
                 "Who wrote 'To Kill a Mockingbird'?",
                 "What is the boiling point of water?",
                 "What is the chemical symbol for gold?"]
    Answers = ["Paris",
               "4",
               "Jupiter",
               "Harper Lee",
               "100°C",
               "Au"]
    
    score = 0
    
    print("Welcome to the Quiz Game!")
    for i in range(len(Questions)):
        print(Questions[i])
        user_answer = input("Your answer: ")
        if user_answer.lower() == Answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is:", Answers[i])
    print("Your final score is:", score)
    if score == len(Questions):
        print("Excellent! You got all questions right!")
    elif score >= len(Questions) / 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")
if __name__ == "__main__":
    Quiz_Game()