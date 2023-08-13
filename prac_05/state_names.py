"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

### TODO: Reformat this file so the dictionary code follows PEP 8 convention
"""CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}
for x, y in CODE_TO_NAME.items():

    print("{short_form:<3} is {long_form}".format(short_form = x, long_form = y))
state = input("Enter short state: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

for x, y in CODE_TO_NAME.items():
    print("{short_form:<3} is {long_form}".format(short_form = x, long_form = y))
state = input("Enter short state: ").upper()