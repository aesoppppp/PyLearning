f = open("proverbs.txt", "r", encoding='UTF-8')
for line in f:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word);

f.close()
