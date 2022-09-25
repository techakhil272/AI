from itertools import count
import random
print("Let the game begin")
data = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}


def display():
    print("Enter Your Choice")
    for f in data:
        print(f, end="=>")
        print(data[f])


def fetch_userchoice():
    display()
    userschoice = input("Man = ")
    userschoice = userschoice.lower()
    #print(userschoice)
    if userschoice == "rock" or userschoice == "r":
        userschoice = 1
    elif userschoice == "paper" or userschoice == "p":
        userschoice = 2
    elif userschoice == "scissors" or userschoice == "s":
        userschoice = 3
    else:
        userschoice = int(userschoice)
    return userschoice


def fetch_machinceschoice():
    machineschoice = random.randint(1, 3)
    return machineschoice


def print_outcome(uc, mc, outcome):
    filename = "Scores.csv"
    fr = open(filename, "a")
    frExist = open(filename, "r").read()
    if (frExist == ''):
        fr.write("UserChoice,"+"Machineschoice,"+"Outcome")
    fr.write("\n"+str(mc)+","+str(uc)+","+outcome)


def fetch_outcome(uc, mc):
    print("Machines Choice: "+str(mc)+"\nUsers Choice: "+str(uc))
    if ((uc == 1 and mc == 3) or (uc == 2 and mc == 1) or (uc == 3 and mc == 2)):
        return ("User Wins")
    elif ((uc == 1 and mc == 2) or (uc == 2 and mc == 3) or (uc == 1 and mc == 3)):
        return ("Machine Wins")
    else:
        return ("Tie")


count = int(input("How many times do you wanna play: "))
i = 1
while (i <= count):
    uc = fetch_userchoice()
    mc = fetch_machinceschoice()
    outcome = fetch_outcome(uc, mc)
    print(outcome+"\n==========================================================================")
    print_outcome(uc, mc, outcome)
    i = i+1
