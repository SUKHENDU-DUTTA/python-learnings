#Syntax of walrus operator

numbers=[1,2,3,4,5,6,7]
while(n:=len(numbers))>0:
    print(numbers.pop())

#Code without using walrus

foods=list()
while True:
    food=input("What food do you like? : ")
    if food == "quit":
        break
    foods.append(food)
print(foods)

#Using walrus operator

foods=list()
while(food := input("What food do you like? :")) != "quit":
    foods.append(food)
print(foods)
