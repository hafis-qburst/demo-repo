#!/bin/python3

#program for counting words in a file.
fname = input('Enter file name: ')
try:
    fhand = open(fname, 'r')
except:
    print('File could not be opened')
    exit()
words = dict()
words2 = dict()

for line in fhand:
    wds = line.split() #strip of lines into words based on whitespace.
    for wd in wds:
        words[wd] = words.get(wd, 0) + 1 #get method almost does what the following code does
        if wd in words2:
            words2[wd] += 1
        else:
            words2[wd] = 1

print(words)
print(words2)

if(words == words2):
    print("Succesful!")

for key in words:
    print(key, words[key])

print("------------------------------------------------------")

#OR
bigword = None
bigcount = 0
for key,value in words2.items():
    print(key, value)
    if value > bigcount:
        bigcount = value
        bigword = key
print('most recurring word is')
print(bigword, bigcount)
