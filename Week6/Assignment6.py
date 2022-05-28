'''
Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
# Use the file name mbox-short.txt as the file name
'''
from itertools import count


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts= dict()
for line in handle:
    if not line.startswith('From'):continue  
    line=line.split()
    if line[0]=='From':
        line =  line[5].split(':')
        for hrs in line[0].split():
            counts[hrs] = counts.get(hrs, 0) +1
                
for key,value in sorted(counts.items()):
    print(key,value)