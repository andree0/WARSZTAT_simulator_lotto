# download module shuffle from library random
from random import shuffle as s

# create a lists
selected_numbers = []
name_numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']

# selecting six numbers and checking if the numbers meet the conditions
for i in range(6):
    while True:
        try:
            selected_numbers.append(int(input(f"Enter a {name_numbers[i]} number: ")))
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
        except ValueError:
            print("""
            It's not a number!
            """)

# sort selected numbers from lowest and show them
selected_numbers.sort()
print(selected_numbers)

# select six numbers between 1 and 49

# create a list of numbers between 1 and 49
all_numbers = [i for i in range(1, 49)]
# shuffle numbers
s(all_numbers)
# choice of the first six numbers
drawn_numbers = all_numbers[0:6]
# display the drawn numbers
print(drawn_numbers)

# create a list of hit numbers
hit_numbers = [i for i in drawn_numbers if i in selected_numbers]

# show number of hits
print(f"""
You hit {len(hit_numbers)} numbers !
""")
