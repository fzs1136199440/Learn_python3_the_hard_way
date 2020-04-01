from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying {from_file} to {to_file}.")

# we could do these two on one line, how?
# we can do this: indata = open(from_file).read()
# in_file = open(from_file)
# indata = in_file.read()
# indata = open(from_file).read()

# print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}.")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()
out_file = open(to_file, 'w')
out_file.write(open(from_file).read())
# open(to_file, 'w').write(open(from_file).read())

# print("Alright, all done.")

# in_file.close()
open(from_file).close()
out_file.close()
# open(to_file, 'w').close()