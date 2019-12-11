read_file = open("test.txt","r")
write_file = open("test1.txt","w+")

titles = []
wrongInputs = []

print("The title of a book will be displayed. Enter a 'y' if you think it is a self-help book. Otherwise enter 'n'. Enter 'x' to exit the program safely.")

if read_file.mode == 'r':
    lines = read_file.readlines()
    for x in lines:
        print(x)
        choice = input("Y or N?")
        print(choice)
        if choice == "y":
            write_file.write(x)
        elif choice == "n":
            continue
        elif choice == "x":
            break
        else:
            wrongInputs.append(x)

write_file.write("Here are the choices you entered an invalid input on\n\n")
for x in wrongInputs:
    write_file.write(x)

read_file.close()
write_file.close()