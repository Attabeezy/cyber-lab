## use open for opening files
file_obj = open("cyberlab.txt", 'r')
cyberlab_content = file_obj.read()
print(cyberlab_content)
file_obj.close()

## using with statement
with open("cyberlab.txt", 'r') as file:
    content = file.read()
    print(content)
    
## writing to a file
with open("output.txt", 'w') as file:
    file.write("Hello, Cyberlab\n")
    file.write("Thsi is a new line.\n")
    

with open('cyberlab.txt', 'r') as file:
    new_content = file.read()
    print(new_content)
    
## writing multiple lines
lines = ["We are learning about python file handling.\n",
         "Python has an easier to read syntax.\n",
         "Python has a huge community of supporters."]
print(lines)

## writing to a new filename
with open("python_community.txt", 'w') as file:
    print(file.read())