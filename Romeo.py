fname = input("Enter file name: ")
fh = open(fname)
line = list()
for line in fh:
    line.sort()
print(line.rstrip())