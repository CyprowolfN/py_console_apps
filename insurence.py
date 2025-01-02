# LOOPS
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for fruit in sorted(set(basket)):
#     print(fruit)

#     basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for fruit in basket:
#     print(fruit)



##INSURENCE

age = int(input("Please enter your age "))

def insurence(age):
    if age < 21:
        print("You don't qualify for insurence")

    elif age == 21 or age <= 54:
        print("You qualify for the premium insurence of R399p/m")

    elif age == 55 or age <=79:
        print("You qualify for the premium insurence of R299p/m")

    elif age == 80 or age <=100:
        print("Wow you're still alive, you qualify for the Gold membership insurence of R199p/m")

    else:
        print("Why are you even alive?")

insurence (age)