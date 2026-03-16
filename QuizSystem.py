import pandas as pd
import random as r
# _Read Questions from above CSV_
# _Prepare 5-10 questions for a quiz_
# A user will come and enter his/her name and take the quiz.
# One user cannot take quiz twice
# Save user score in a different csv named as student score
# if a student fail any question game will be end instantly

questionare = pd.read_csv("QuestionareDummy.csv")
import random as r
randomnumberList = []
for i in range(10):
    while True:
        random10Numbers = r.randint(0,20)
        if random10Numbers not in randomnumberList:
            randomnumberList.append(random10Numbers)
            break
        else:
            continue
# for questionnumbers in randomnumberList:
#     print(questionare.loc[questionnumbers])


userdataDictionary = {"Names":["Ahmad","Ali","Pyth"],"Score":[9,10,5]}

userDataFrame = pd.DataFrame(userdataDictionary)
while True:
    print("Enter 1 if you are new and want to take the test Enter 2 For taking the test again \nenter 3 for exit")
    choice = input("Enter your choice:")
    if choice == "1":
        name = input("Enter your name:")
        # Quiz Proceed

    elif choice == "2":
        name = input("Enter your name:")
        if name in list(userDataFrame["Names"]):
            # Quiz proceed
    elif choice == "3":
        break
    else :
        pass
