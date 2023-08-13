
COLOUR_CODES = {"absolutezero": "#0048ba", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "alizarincrimson": "#e32636", "apricot": "#fbceb1",
                "eggshell": "#f0ead6", "fawn": "#e5aa70",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_nametwo = input("Enter a colour name: ")
colour_name = colour_nametwo.lower()
while colour_name != "":
    print("The hex for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
