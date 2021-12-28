""" To do this, count the number of times a depth measurement increases from the previous measurement.
(There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?
"""

#open file
with open("day1input.txt", "r") as f:
    input = f.read() # Read all file in case values are not on a single line
    input_ints = [ int(x) for x in input.split() ] # Convert strings to ints

#set up variables
previous = input_ints[0]
numIncreases = 0

#do math
for i in input_ints:
    current = i
    if current > previous:
        numIncreases = numIncreases + 1
    previous = current

#day 1 output
print("day 1: " + str(numIncreases))

#day 2 start
#set up variables
previous = input_ints[0] + input_ints[1] + input_ints[2]
numIncreases = 0

#do math
for i in range(len(input_ints) - 3):
    current = input_ints[i] + input_ints[i + 1] + input_ints[i + 2]
    if current > previous:
        numIncreases = numIncreases + 1
    previous = current

#day 2 output
print("day 2: " + str(numIncreases))
