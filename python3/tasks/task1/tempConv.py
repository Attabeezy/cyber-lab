"""
This is a script for converting
between Celsius(C), Fahrenheit (F), and Kelvin(K)
"""

F = ""
C = ""
K = ""

conv_op = input("Please choose\nCF for Celsius-Fahrenheit\nFC for Fahrenheit-Celsius\nCK for Celsius-Kelvin\nKC for Kelvin-Celsius\nFK for Fahrenheit-Kelvin\nKF for Kelvin-Fahrenheit\nEnter: ")

def temp_converter(conv_op):
"""
function for selecting and
converting between temperatures
"""
    if conv_op == "CF":
        C = int(input("Enter Celsius: "))
        F = (9/5 * C) + 32
        print(F, "F")
    if conv_op == "FC":
        F = int(input("Enter Fahrenheit: "))
        C = (F - 32) * 5/9
        print(C, "C")
    if conv_op == "CK":
        C = int(input("Enter Celsius: "))
        K = C + 273.15
        print(K, "K")
    if conv_op == "KC":
        K = int(input("Enter Kelvin: "))
        C = K - 273.15
        print(C, "C")
    if conv_op == "FK":
        F = int(input("Enter Fahrenheit: "))
        K = ((F - 32) * 5/9) + 273.15
        print(K, "K")
    if conv_op == "KF":
        K = int(input("Enter Kelvin: "))
        F = ((K - 273.15) * 9/5) + 32
        print(F, "F")


try:
    temp_converter(conv_op)
except NameError:
    print("try again!!")

