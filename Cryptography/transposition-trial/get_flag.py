#!/usr/bin/env python3
file = open("message.txt", "r").read()
print(file) #print our message

flag = ""
for n in range(0, len(file), 3):
    blocks = file[n: n + 3]
    flag += blocks[2] + blocks[0:2]

print(flag)