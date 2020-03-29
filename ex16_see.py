from sys import argv

script, filename = argv

t = open(filename)

print(t.read())
t.close()