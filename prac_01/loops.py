# add this for loop that displays all of the odd numbers between 1 and 20 with a space between each one
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count in 10s from 0 to 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#  print n stars. Ask the user for a number, then print that many stars (*), all on one line
number_of_stars = int(input("Number of stars = "))
for i in range(0, number_of_stars):
    print("*", end=' ')
print()

# print n lines of increasing stars
number_of_stars = int(input("Number of stars = "))
for i in range(1, number_of_stars+1):
    print("*"*i)
print()