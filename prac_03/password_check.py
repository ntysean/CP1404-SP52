

def main():
    minimum_length, password = get_password()
    while len(password)<minimum_length:
        print("Invalid password. too short.")
        password = input("Enter another password:")
    else:
        print_asterisks(password)

def print_asterisks(password):
    for i in range(0, len(password)):
        print("*", end="")


def get_password():
    minimum_length = int(input("minimum password length is:"))
    password = input("Enter the password:")
    return minimum_length, password

main()


