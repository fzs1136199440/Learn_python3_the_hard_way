from sys import argv
from os.path import exists

script, from_file, to_file = argv

# open(from_file).read()

print(f"Does the output file exist? {exists(to_file)}")
print("If not, created it.")

open(to_file, 'w').write(open(from_file).read())

open(from_file).close()
open(to_file, 'w').close()
print('Done.')