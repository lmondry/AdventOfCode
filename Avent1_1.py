#!/usr/bin/env python

f = open("data/input.txt","rb+")
changes = []
for i in f:
    changes.append(int(i))
frequency = 0
for change in changes:
    frequency = frequency + change
print frequency