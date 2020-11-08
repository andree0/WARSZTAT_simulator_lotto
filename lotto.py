# download module shuffle from library random
from random import shuffle as s

selected_numbers = []
name_numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
for i in range(6):
    while True:
        try:
            selected_numbers.append(int(input(f"Enter a {name_numbers[i]} number")))
            if 0 < selected_numbers[i] < 50:
                if selected_numbers[i] in selected_numbers:
                    break
                else:
                    selected_numbers.pop(i)
                    print("""
                    You already entered that number!
                    Choose a different number.
                    """)
            else:
                selected_numbers.pop(i)
                print("""
                The number is out of range!
                You have to select number between 1 and 49.
                """)
            # break
        except ValueError:
            print("It's not a number!")

print(selected_numbers)

# 3.

# select six numbers between 1 and 49
all_numbers = [i for i in range(1, 49)]
s(all_numbers)
drawn_numbers = all_numbers[0:6]
print(drawn_numbers)
