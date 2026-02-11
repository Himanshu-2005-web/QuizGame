print("Welcome To The Quiz Game!")
question_bank=[
    {"text":"The ability of one class to acquire methods and attributes from another class is called.","answer":"A"},
    {"text":"Which of th following is a type of inheritance?","answer":"D"},
    {"text":"What type of inheritance has multiple Subclass to a single superclass?","answer":"C"},
    {"text":"What is the depth of multilevel inheritance in python?","answer":"C"},
    {"text":"What does MRO stands for?","answer":"B"}
]
options=[["A. Inheritance","B. Abstraction","C. Polymorphism","D. Objects"],
         ["A. Single","B. Double","C. Multiple","D. Both A and C"],
         ["A. Multiple inheritance","B. Multilevel inheritance","C. Hierarchical inheritance","D. None"],
         ["A. Two level","B. Three level","C. Any level","D. None"],
         ["A. Method Recursive Object","B. Method Resolution Order","C. Main Resolution Order","D. None"]

]

score=0
def check_ans(user_guess,correct_ans):
    if user_guess==correct_ans:
        return True
    else:
        return False
    
for question_num in range(len(question_bank)):
    print("-----------------------------------------------------------")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess=input("Enter your answer(A/B/C/D):").upper()    
    is_correct=check_ans(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer.")
        score+=1
    else:
        print("Worng answer.")  
        print(f"The correct answer is {question_bank[question_num]['answer']}") 

print(f"Your have give {score} correct answers")     
print(f"Your Score is {(score/len(question_bank))*100}%")    