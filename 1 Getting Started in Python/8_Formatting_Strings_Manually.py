formatter = "{} {} {} {}"

#using the .format we can add eany value in to the {} in order and if we try to add the formader string it will just be put in as a string containing the tekst {}
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
#prints the lines as wtitten with new lines as in the code
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))