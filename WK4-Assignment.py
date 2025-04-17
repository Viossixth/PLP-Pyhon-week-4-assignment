def file_handling_function():
    filename=input("Instructions.txt")

try:
    with open("Instructions.txt","r") as file:
        data=file.read()

    modified_content= file.upper()

    new_file = f"modified_{'New-Instructions.txt'}"

    with open("New-Instructions.txt","w") as file:
        new_file.write("modified")

    print (f"modified Instructions to {'New-Instructions'}")
    
except FileNotFoundError:
    print("File not found.")
