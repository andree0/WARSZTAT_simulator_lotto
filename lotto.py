# download module shuffle from library random
from random import shuffle as s

# create a lists
selected_numbers = []
name_numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
i = 0
# selecting six numbers and checking if the numbers meet the conditions
while i < 6:
    # try to change value input from string to int
    try:
        number = int(input(f"Enter a {name_numbers[i]} number: "))
    except ValueError:
        number = 0
        print("""
            It's not a number!
            """)
    # condition that the number is between 1 and 49
    # condition that the number is not repeated
    # add a number to list
    if number not in selected_numbers and 0 < number < 50:
        selected_numbers.append(number)
        i += 1
    else:
        print("""
            Number have to between 1 and 49.
            Numbers must not be repeated.
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
# sort and display the drawn numbers
drawn_numbers.sort()
print(drawn_numbers)

# create a list of hit numbers
hit_numbers = [i for i in drawn_numbers if i in selected_numbers]

# show number of hits
print(f"""
            You hit {len(hit_numbers)} numbers !
""")
