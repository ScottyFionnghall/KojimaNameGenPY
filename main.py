import random

f = open("questions.txt",'r',encoding='utf-8')
qst = f.read()
f.close
qst = qst.split('\n')
answers = []
states = []
category = random.randint(1,20)

# generate name based on the category
def nameGen():
    name = ''
    if category  in range(2,6):
        print("Your name is from Occupational category")
        name = ocupname[random.randint(0,3)] + " " +answers[1]
    elif category in range(7,10):
        print("Your name is from Horny category")
        name = hornyname[random.randint(0,3)] +" " + answers[2]
    elif category in range(11,13):
        print("Your name is from THE category")
        name = "The " + thename[random.randint(0,3)]
    elif category in range(14,17):
        print("Your name is from Cool category")
        name = answers[20] + " " + coolname[random.randint(0,5)]
    elif category in range(18,19):
        print("Your name is from Violent category")
        name = violentname[random.randint(0,3)] + " " + answers[4]
    elif category == 20:
        print("You have name that lacks subtext")
        name = answers[9]
    else:
        print("You hava a normal name")
        name = answers[0]
    return name

# add conditions
def conditName(name):
    if category not in range(18,19):
        if states[1] == 4:
            print("You have MAN condition")
            name = name + "man"
        if states[2] == 6:
            print("You have CONDITION condition (BIG)")
            name = "Big " + name
        elif states[2] == 7:
            print("You have CONDITION condition (OLD)")
            name = "Old " + name
        elif states[2] == 8:
            print("You have CONDITION condition (how you currently are)")
            name = answers[10] + " " + name
        if states[3] == 69:
            print("You are Hideo Kojima! (ignore text before)")
            name = "Hideo Kojma"
    return name

for i in range(0,len(qst)):
    print(qst[i])
    answers.append(input())

states.append(random.randint(1,6))
states.append(random.randint(1,4))
states.append(random.randint(1,8))
states.append(random.randint(1,12))
states.append(random.randint(1,100))

ocupname = [answers[14],answers[5],answers[12],answers[15]]
hornyname = [answers[11],'Naked',answers[5],answers[13]]
thename = [answers[7],answers[8],answers[3],answers[19]]
coolname = [answers[16],answers[17],answers[18],answers[5],answers[7],answers[12]]
violentname = [answers[18],answers[11],answers[19],answers[8]]

if states[0] == 6:
    for i in range(0,6):
        print("You have 6 names")
        final = conditName(nameGen())
        print("\nYour name is: ",final)
else:
    final = conditName(nameGen())
    print("\nYour name is: ",final)