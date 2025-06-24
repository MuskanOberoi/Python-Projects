Questions = [{"Question" : "Which is the largest planet?",
              "Options" : {"A" : "Mars", "B" : "Jupiter" , "C" : "Earth"}, 
              "Answer": "B"
              },
              {
              "Question" :" King of Fruits?",
              "Options" : {"A" : "Mango", "B" : "Apple", "C" : "Grapes"},
              "Answer" : "A"
              },
              {
              "Question" : "king of jungle?",
              "Options" : {"A" : "Bear", "B" : "Monkey", "C" : "Lion"},
              "Answer" : "C"
              },
            {
              "Question" : "Capital of India?",
              "Options" : {"A" : "Chandigarh", "B": "New Delhi", "C" : "Goa"},
              "Answer" : "B"
              }
]
            
points = 0
for q in Questions:
    print(q["Question"]) #TO PRINT QUESTION
    for key , value in q["Options"].items(): #TO PRINT OPTIONS
        print(f"{key}.{value}")
              
    answer = input("Enter your Answer(A,B,C):")#TO PRINT ANSWER
    if answer == q["Answer"]:
       print("You are Correct!!")
       points+=1
    else:
       print(f"Incorrect!! The correct answer is {q['Answer']}: {q['Options'][q['Answer']]}")
print(f"Your Score is {points}/{len(Questions)}")