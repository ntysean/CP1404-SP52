OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE,'w')
name = input("What is your name? : ")
print(name, file = out_file)
out_file.close()


in_file = open(OUTPUT_FILE, "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)


in_file = open("numbers.txt", "r")
### you can use a file containing any number of numbers in place of numbers.txt
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)