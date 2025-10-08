"""
Program to read text file and counts words, lines, and characters
Should also ask user to enter new lines and view number of words, lines, and character

- view text file
- add new lines
- total count of:
    words,
    lines,
    characters
"""

def viewText():
    with open("text.txt", 'r') as file:
        lines = file.readlines()
        print("-" * 35)
        for index, line in enumerate(lines, start=1):
            print(f"{index}~ {line.strip()}")
        print("-" * 35)

def addText(newText):
    with open("text.txt", 'a') as file:
        file.writelines(f"{str(newText).strip()}")
    print(f"new line added!")
    return

def removeText(line_number):
    with open("text.txt", 'r') as file:
        lines = file.readlines()
    
    if len(lines) == 0:
        print("No lines!")
        return
    
    if line_number < 1 or line_number > len(lines):
        print("Invalid Line Number")
        return
    
    removed = lines[line_number - 1].strip()
    lines.pop(line_number - 1)
    
    with open("text.txt", 'w') as file:
        file.writelines(lines)
        print(f"'{removed.strip()}' removed!")

def countText():
    """
    total count of:
    words,
    lines,
    characters
    """
    try:
        with open("text.txt", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    lines_string = ''.join(lines)
    
    ## word count
    words = lines_string.split()
    word_count = len(words)
    print(f"total words: {str(word_count)}")
    
    ## line count
    line_count = len(lines)
    print(f"total lines: {str(line_count)}")
    
    ## character count
    # words with spaces and punctuation
    char_with_spaces = len(lines_string)
    print(f"characters with spaces: {char_with_spaces}")
    
    # Remove all whitespace and punctuation to count only characters
    words_only = ''.join(lines_string.split())
    char_only = len(words_only)
    print(f"characters without spaces: {char_only}")
    

def quit():
    print("exiting....")
    exit()

def main():
    ## tasks inputs, logic check, etc
    while True:
        opt = input("Choose an option - view, add, remove, stats, quit: ")
        if opt == "view":
            viewText()
        elif opt == "add":
            new_line = input("Enter the new line to add: ")
            addText(new_line)
        elif opt == "remove":
            try:
                line_number = int(input("Enter the line number to remove: "))
                removeText(line_number)
            except ValueError:
                print("Please enter a valid integer for the line number.")
        elif opt == "quit":
            quit()
        elif opt == "stats":
            countText()
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()