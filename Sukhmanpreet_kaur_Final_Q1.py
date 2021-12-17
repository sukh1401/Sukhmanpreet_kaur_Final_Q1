lines = []
with open('PROG1783File1Before.txt') as firstFile, open('PROG1783File1After.txt', 'w') as secondFile:
    lines = firstFile.readlines()
    line = lines[0]
    characters = line[0:100]
    secondFile.write(characters)
