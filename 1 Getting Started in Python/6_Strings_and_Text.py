
#make a variabel with the int 10
types_of_people = 10
#make a string with the int variabel types_of_people after are with a f string
x = f"There are {types_of_people} types of people."    # 2
#make more variabels with strings
binary = "binary"
do_not = "don't"
#use a f string to ad the 2 last strings in to the sring in the varabel y
y = f"Those who know {binary} and those who {do_not}."    # 2

#print the strings
print(x)
print(y)

#print the strings with som tekst in front using a f string
print(f"I said: {x}")    # 2
print(f"I also said: '{y}'")    # 2

#bake a variabel with a bool
hilarious = False
#make a variabel with a string that can add somting were the {} are
joke_evaluation = "Isn't that joke so funny?! {}"

# print the sting and format it with the variabel hilariou to adde it in
print(joke_evaluation.format(hilarious))

# make to variabels with strings
w = "This is the left side of..."
e = "a string with a right side."

# add w and e together and print it
print(w + e)