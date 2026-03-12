import random

def check(comp,user):
    if comp==user:
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==2 and user==0):
        return -1
    if(comp==2 and user==0):
        return -1
    if(comp==2 and user==1):
        return -1
    
    return 1

comp=random.randint(0,2)
user=int(input("Enter 0 for Snake, 1 for Water and 2 for Gun."))

score=check(comp,user)

print("You: ",user)
print("COmputer: ",comp)
if(score==0):
    print("It's draw.")
elif(score==-1):
    print("You LOSE")
else:
    print("You Won")