#Function checks name is letters only
def nameIsAlpha():
    while True:
        name = input("What is your name?: ")
        if name.isalpha():
            return name
        else:
            print("Invalid character, please try again")


print("Hello World")
name = nameIsAlpha()
print("A pleasure to meet you '" + name + "'") 
