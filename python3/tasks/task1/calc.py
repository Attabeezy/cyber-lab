while True:
    calc_input = input("CASIO ES-95000 \nEnter: ")
    if calc_input != "q":
        try:
            print(eval(calc_input))
        except NameError:
            print("Enter a valid number!!!")
    else:
        break
