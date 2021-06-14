infile = open("phones.txt", "r", encoding='UTF-8')
line = infile.readline().rstrip()

while line != "":  # for line in infile: 로도 할 수 있다
    print(line)
    line = infile.readline().rstrip()

infile.close()
