print("------- Quiz Game ------")

ques = {
    "Who is known as the father of computers": "charles babbage",
    "Python was created by": "Guido van Rossum",
    "capital of India": "Delhi"
}

for q,ans in ques.items():
    user = input(q).lower()
    if user ==ans:
        print("correct!")
        score +=1
    else:
        print("wrong!")

total = len(ques)
percentage = (score/total)*100
print("Your final score:", score, "/", total)
print('percentage:', round(percentage,2), '%') 