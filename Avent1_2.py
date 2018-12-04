#!/usr/bin/env python

f = open("data/input.txt","rb+")
changes = []
for i in f:
    changes.append(int(i))
frequency = 0
seenFrequency = []
notFound = True
while notFound:
    for change in changes:
        if frequency not in seenFrequency:
            seenFrequency.append(frequency)
            frequency = frequency + change
            print frequency
        else:
            notFound = False
print frequency