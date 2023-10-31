# Creating Rock Paper Scissors Game in Python
import random


menu = " Rock Paper Scissors Game " # displaying Menu
print("\n", menu.center(40, "-"), end="\n\n")

rnd_list = ["Rock", "Paper", "Scissors"] # list
cnt = 0
# Displaying choices
for i in rnd_list: 
    print("\t", str(cnt).ljust(4, '-'), i)
    cnt += 1

# new line
print("")

# total attemps
attempt = 0

cmp_score = 0 # computer's score
usr_score = 0 # user's score

while attempt != 3: # Total 3 attempts 

    attempt += 1 # incriment by 1
    cmp_choice = random.choice(rnd_list) # computer chooses randomly

    usr_choice = int(input("\n\tEnter your choice: ")) # take input from user
    while not (usr_choice >= 0 and usr_choice <= 2):  
        usr_choice = int(input("\n\tTry again!: ")) # take input from user

    print("\n\t[USER] Chooses: ", rnd_list[usr_choice])
    print("\t[CMPT] Chooses: ", cmp_choice, end="\n\n")



    if cmp_choice == "Rock" and rnd_list[usr_choice] == "Paper":
        print("\t[CMPT] WINS!")
        cmp_score += 1

    elif cmp_choice == "Paper" and rnd_list[usr_choice] == "Rock":
        print("\t[USER] WINS!")
        usr_score += 1
    
    elif cmp_choice == "Rock" and rnd_list[usr_choice] == "Scissors":
        print("\t[CMPT] WINS!")
        cmp_score += 1

    elif cmp_choice == "Scissors" and rnd_list[usr_choice] == "Rock":
        print("\t[USER] WINS!")
        usr_score += 1

    elif cmp_choice == "Paper" and rnd_list[usr_choice] == "Scissors":
        print("\t[CMPT] WINS!")
        cmp_score += 1

    elif cmp_choice == "Scissors" and rnd_list[usr_choice] == "Paper":
        print("\t[USER] WINS!")
        usr_score += 1
    
    else: #if booth chooses same then attempt doesn't count
        print("\tWithdraw!")
        attempt -= 1


# Let's see who wins

if usr_score > cmp_score:
    print("\n\tThe Winner is....  [USER]\n")
else:
    print("\n\tThe Winner is....  [CMPT]\n")
