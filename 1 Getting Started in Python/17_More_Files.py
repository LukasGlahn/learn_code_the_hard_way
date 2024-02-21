from os.path import exists

# we could do these two on one line, how?
in_file = open("test.txt")
indata = in_file.read()

out_file = open("new_test.txt", 'w')
out_file.write(indata)

