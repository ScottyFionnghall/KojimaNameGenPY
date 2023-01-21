import random
# open file questions.txt that contains every question
# and put it in a qst variable
f = open("questions.txt",'r',encoding='utf-8')
qst = f.read()
f.close
qst = qst.split('\n')
# here we define empty lists for later use
answers = []
states = []
# generate name based on the category
# every catergory falls in a range between numbers so
# i couldnt find any better way than to use a lot of
# if statments
# 
# also i use f-strings because it's easier than
# changing every variable type to string
def nameGen():
    # i define empty name variable to return it later
    # 
    # some categories also have multiple variations so
    # i generate random number (equal to dice roll)
    # to select part of the name from later defined
    # variables
    name = ''
    if category  in range(2,6):
        print("Your name is from Occupational categor")
        name = f"{ocupname[random.randint(0,3)]} {answers[1]}"
    elif category in range(7,10):
        print("Your name is from Horny category")
        name = f"{hornyname[random.randint(0,3)]} {answers[2]}"
    elif category in range(11,13):
        print("Your name is from THE category")
        name = f"The {thename[random.randint(0,3)]}"
    elif category in range(14,17):
        print("Your name is from Cool category")
        name = f"{answers[20]} {coolname[random.randint(0,5)]}"
    elif category in range(18,19):
        print("Your name is from Violent category")
        name = f"{violentname[random.randint(0,3)]} {answers[4]}"
    elif category == 20:
        print("You have name that lacks subtext")
        name = answers[9]
    else:
        print("You hava a normal name")
        name = answers[0]
    return name
# this functions adds conditions
def conditName(name):
    # i have to use this if statement because
    # violent category does not contain any conditions
    if category not in range(18,19):
        if states[1] == 4:
            print("You have MAN condition")
            name = f"{name}man"
        if states[2] == 6:
            print("You have CONDITION condition (BIG)")
            name = f"Big {name}"
        elif states[2] == 7:
            print("You have CONDITION condition (OLD)")
            name = f"Old {name}"
        elif states[2] == 8:
            print("You have CONDITION condition (how you currently are)")
            name = f"{answers[10]} {name}"
        if states[3] == 69:
            print("You are Hideo Kojima! (ignore text before)")
            name = "Hideo Kojma"
    return name
# main for loop to go through every questions and
# put answers into answers variable by appending it
# at the end
for i in range(0,len(qst)):
    print(qst[i])
    answers.append(input())
    
# 5 dice rolls for conditions NEED TO MAKE BETTER
states.append(random.randint(1,6))
states.append(random.randint(1,4))
states.append(random.randint(1,8))
states.append(random.randint(1,12))
states.append(random.randint(1,100))
# this variables(lists) contain all different parts
# of a name that randomly chosen when deciding on
# name category
ocupname = [answers[14],answers[5],answers[12],answers[15]]
hornyname = [answers[11],'Naked',answers[5],answers[13]]
thename = [answers[7],answers[8],answers[3],answers[19]]
coolname = [answers[16],answers[17],answers[18],answers[5],answers[7],answers[12]]
violentname = [answers[18],answers[11],answers[19],answers[8]]
# to add ability to generate new name i put everithing
# into infinte loop and when user writes "n", programm exits
while True:
    category = random.randint(1,20)
    final = conditName(nameGen())
    print("\nYour name is: ",final.title())
    if input("Try new name? Y/n\n").lower() == "y":
        pass
    else:
        break
