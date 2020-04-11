from sys import argv

script, fn = argv
f = open(fn, 'r+')
f.write("ddddddddd")
f.close()