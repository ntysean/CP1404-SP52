name = input("Enter name: ")
print("""
(H)ello
(G)oodbye
(Q)uit""")
      
choice = input()
while choice != "Q":
    if choice == "H":
        print("Hello "+name)
    elif choice == "G":
        print("Goodbye "+name)

    else:
        print("Invalid message")
    print("""
(H)ello
(G)oodbye
(Q)uit""")
    break
