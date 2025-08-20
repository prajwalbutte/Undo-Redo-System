print("Welcome To Undo-Redo System\n")
undo_stack = []
redo_stack = []


def Make_Change():
    text = input(("Enter String: "))
    undo_stack.append(text)
    redo_stack.clear()


def undo():
    if undo_stack:
        x = undo_stack.pop()
        redo_stack.append(x)
    else:
        print("Nothing to undo\n") 
        


def redo():
    if redo_stack:
        x = redo_stack.pop()
        undo_stack.append(x)
    else:
        print("Nothing to redo\n")
        
        


def display():
    for i in undo_stack:
        print(i, end=" ")
    print("\n")

    
print("----Menu----\n")

while(True):
    print("1.Make Changes\n")
    print("2.Undo\n")
    print("3.Redo\n")
    print("4.Display\n")
    print("5.Exit\n")

    choice = int(input("Enter your Choice:"))    
    if choice == 1:
        Make_Change()
    elif choice == 2:
        undo()
    elif choice == 3:
        redo()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Thank You For Using...!\n")
        break
    else:
        print("Invalid Choice\n")