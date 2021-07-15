student = []
status = True
while status:
    print(" Press 1 : For add students \n Press 2 : For students list \n Press 3 : For update student \n Press 4 : For delete student \n Press 5 : Exit" )
    choice = int(input("Enter your choice:  "));print()
    
    if choice == int(1):
        name = input("Enter student name: ")
        student.append(name)
        print(student)

    elif choice == int(2): 
        print(student) 

    elif choice == int(3):
        n=int(input("Enter student number:"))
        name = input("Enter student name: ")
        student[n]=name
        print(student)       

    elif choice == int(4):
        n=int(input("Enter student number:"))
        name = input("Enter name:")
        del student[n]
        print(student)

    elif choice == int(5):
        print("Thank you !!!")
        

    c = input("Do you want to continue :")
    print()
    if c == 'y' or c == 'Yes':
        status = True
    else:
        status = False
