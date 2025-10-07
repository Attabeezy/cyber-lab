## Task 1

with open("data.txt", 'w') as file:
    for i in range(1, 11):
        file.write(f"{i}\n")
    
    
with open("data.txt", 'r') as file:
    file_content = file.read()
    print(file_content)

first_name = input("First Name: ")
last_name = input("Last Name: ")
program = input("Program: ")
year = input("Year: ")

info = [f"{first_name} {last_name}\n", f"{program}\n", f"{year}\n"]

with open("data.txt", 'a') as file:
    file.writelines(info)

with open("data.txt", 'r') as file:
    file_content = file.read()
    print(file_content)
    
