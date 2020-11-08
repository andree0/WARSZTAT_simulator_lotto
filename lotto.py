# download module shuffle from library random
from random import shuffle as s

selected_numbers = []

while True:
    try:
        selected_numbers.append(int(input("Enter a first number")))
        while True:
            try:
                selected_numbers.append(int(input("Enter a second number")))
                while True:
                    try:
                        selected_numbers.append(int(input("Enter a third number")))
                        while True:
                            try:
                                selected_numbers.append(int(input("Enter a fourth number")))
                                while True:
                                    try:
                                        selected_numbers.append(int(input("Enter a fifth number")))
                                        while True:
                                            try:
                                                selected_numbers.append(int(input("Enter a sixth number")))
                                                break
                                            except (ValueError, TypeError):
                                                print("It's not a number!")
                                        break
                                    except (ValueError, TypeError):
                                        print("It's not a number!")
                                break
                            except (ValueError, TypeError):
                                print("It's not a number!")
                        break
                    except (ValueError, TypeError):
                        print("It's not a number!")
                break
            except (ValueError, TypeError):
                print("It's not a number!")
        break
    except (ValueError, TypeError):
        print("It's not a number!")

print(selected_numbers)

# 3.

# select six numbers between 1 and 49
all_numbers = [i for i in range(1, 49)]
s(all_numbers)
drawn_numbers = all_numbers[0:6]
print(drawn_numbers)
